class PatternHandler:
    def __init__(self, successor = None):
        self.successor = successor

    def handle(self, grammar_tree, parent_child, root):
        res = self._handle(grammar_tree, parent_child, root)
        if not res and self.successor:
            return self.successor.handle(grammar_tree, parent_child, root)
        else:
            print(self.__class__)
            return res

    def _handle(self, grammar_tree, parent_child, root):
        raise NotImplementedError('Must provide implementation in subclass.')

# ATT SVB HED VOB
class Pattern1(PatternHandler):
    def _handle(self, grammar_tree, parent_child, root):
        attribute, entity = '', ''
        if grammar_tree[parent_child[root][0]]['relate'] != 'SBV' or grammar_tree[parent_child[root][-1]]['relate'] !='VOB':
            return None
        attrib_id = parent_child[root][0]
        attribute = grammar_tree[attrib_id]['cont']
        if not parent_child.get(parent_child[root][0]):
            return None
        entity_id = parent_child[parent_child[root][0]][0]
        has_rad = False
        if not parent_child.get(entity_id):
            return None
        for child in parent_child[entity_id]:
            if grammar_tree[child]['relate'] == 'RAD':
                has_rad = True
        if has_rad:
            if parent_child.get(entity_id) and len(parent_child[entity_id]) <= 2:
                entity += grammar_tree[entity_id]['cont']
            # 递归拼接entity
            while parent_child.get(entity_id):
                if grammar_tree[parent_child[entity_id][0]]['relate'] == 'ATT':
                    entity = grammar_tree[parent_child[entity_id][0]]['cont'] + entity
                    entity_id = parent_child[entity_id][0]
                else:
                    break
            if parent_child.get(attrib_id) and grammar_tree[parent_child[attrib_id][-1]]['relate'] == 'ATT':
                attr_rad = False
                if parent_child.get(parent_child[attrib_id][-1]):
                    for child in parent_child.get(parent_child[attrib_id][-1]):
                        if grammar_tree[child]['relate'] == 'RAD':
                            attr_rad = True
                if not attr_rad:
                    attribute = grammar_tree[parent_child[attrib_id][-1]]['cont'] + attribute
            return entity, attribute

class Pattern2(PatternHandler):
    def _handle(self, grammar_tree, parent_child, root):
        attribute, entity = '', ''
        if len(parent_child[root]) > 1:
            entity_id = parent_child[root][0]
            attr_id   = parent_child[root][1]
            if grammar_tree[entity_id]['relate'] == 'SBV' and grammar_tree[attr_id]['relate'] == 'VOB':
                entity += grammar_tree[entity_id]['cont']
                while parent_child.get(entity_id):
                    if grammar_tree[parent_child[entity_id][0]]['relate'] == 'ATT':
                        entity = grammar_tree[parent_child[entity_id][0]]['cont'] + entity
                        entity_id = parent_child[entity_id][0]
                    else:
                        break
                if parent_child.get(attr_id):
                    attr_id = parent_child[attr_id][0]
                    att_has_rad = False
                    if not parent_child.get(attr_id):
                        return None
                    for child in parent_child[attr_id]:
                        if grammar_tree[child]['relate'] == 'RAD':
                            att_has_rad = True
                    if att_has_rad and grammar_tree[attr_id]['relate'] == 'ATT':
                        attribute = grammar_tree[attr_id]['cont']
                        return entity, attribute

#
class Pattern3(PatternHandler):
    def _handle(self, grammar_tree, parent_child, root):
        attribute, entity = '', ''
        if grammar_tree[parent_child[root][0]]['relate'] != 'SBV' or grammar_tree[parent_child[root][-1]]['relate'] !='VOB':
            return None
        attribute = grammar_tree[parent_child[root][0]]['cont']
        if not parent_child.get(parent_child[root][0]):
            return None
        attrib_id = parent_child[root][0]
        if not parent_child.get(parent_child[root][0]):
            return None
        entity_id = parent_child[parent_child[root][0]][0]
        entity += grammar_tree[entity_id]['cont']
        # 递归拼接entity
        while parent_child.get(entity_id):
            if grammar_tree[parent_child[entity_id][0]]['relate'] == 'ATT':
                entity = grammar_tree[parent_child[entity_id][0]]['cont'] + entity
                entity_id = parent_child[entity_id][0]
            else:
                break
        if parent_child.get(attrib_id) and grammar_tree[parent_child[attrib_id][-1]]['relate'] == 'ATT':
            attr_rad = False
            if parent_child.get(parent_child[attrib_id][-1]):
                for child in parent_child.get(parent_child[attrib_id][-1]):
                    if grammar_tree[child]['relate'] == 'RAD':
                        attr_rad = True
            if not attr_rad:
                attribute = grammar_tree[parent_child[attrib_id][-1]]['cont'] + attribute
        return entity, attribute

class Pattern4(PatternHandler):
    def _handle(self, grammar_tree, parent_child, root):

        if grammar_tree[root]['pos'] not in ["n"] or not parent_child.get(root) or len(parent_child[root]) < 1:
            return None
        if grammar_tree[parent_child[root][0]]['relate'] != 'ATT':
            return None

        entity, attribute = '', ''
        entity_id = parent_child[root][0]
        attrib_id = root

        entity    = grammar_tree[entity_id]['cont'] + entity
        while parent_child.get(entity_id):
            entity_id = parent_child[entity_id][0]
            if grammar_tree[entity_id]['relate'] == 'ATT':
                entity = grammar_tree[entity_id]['cont'] + entity
            else:
                break
        attribute = grammar_tree[attrib_id]['cont'] + attribute
        if len(parent_child[root]) > 1:
            attrib_id = parent_child[root][-1]
            attribute = grammar_tree[attrib_id]['cont'] + attribute
            while parent_child.get(attrib_id):
                attrib_id = parent_child[attrib_id][0]
                if grammar_tree[attrib_id]['relate'] == 'ATT':
                    attribute = grammar_tree[attrib_id]['cont'] + attribute
                else:
                    break
        return entity, attribute


