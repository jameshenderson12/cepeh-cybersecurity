# from rasa.shared.core.slots import Slot
#
# class ConfidenceRatingScale(Slot):
#
#     def feature_dimensionality(self):
#         return 2
#
#     def as_feature(self):
#         r = [0.0] * self.feature_dimensionality()
#         if self.value:
#             if self.value <= 10:
#                 r[0] = 1.0
#             else:
#                 r[1] = 1.0
#         return r
