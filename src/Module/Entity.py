import jieba
import numpy as np

class Entity:
    def __init__(self, entity):
        self.entity = entity

    def getAnswer(self, target_attribute, word_embeddings):

        if self.entity.get(target_attribute):
            return target_attribute, self.entity[target_attribute], 1.0

        # 组合target attribute 的embedding
        words = jieba.cut(target_attribute)
        target_vec = [0]*300
        for word in words:
            if word_embeddings.get(word):
                target_vec = np.add(target_vec, word_embeddings[word])

        # 找到与target attribute最相近的entity attribute
        max_similarity = 0
        max_attribute  = ''
        for attribute in self.entity:
            attribute_vec = [0]*300
            words = jieba.cut(attribute)
            for word in words:
                if word_embeddings.get(word):
                    attribute_vec = np.add(attribute_vec, word_embeddings[word])

            if sum(target_vec) == 0 or sum(attribute_vec) == 0:
                return None
            similarity = np.dot(attribute_vec, target_vec) / (np.linalg.norm(attribute_vec) * np.linalg.norm(target_vec))
            if similarity > max_similarity:
                max_similarity = similarity
                max_attribute  = attribute

        if max_similarity < 0.5:
            return None
        return max_attribute, self.entity[max_attribute], max_similarity

    def getAnswerFromMultiTarget(self, target_attributes, word_embeddings):
        max_attribute  = ''
        max_similarity = 0
        max_value = ''
        for target_attribute in target_attributes:
            attribute, value, similarity = self.getAnswer(target_attribute, word_embeddings)
            if max_similarity < similarity:
                max_similarity = similarity
                max_attribute  = attribute
                max_value      = value
        return max_attribute, max_value ,max_similarity
