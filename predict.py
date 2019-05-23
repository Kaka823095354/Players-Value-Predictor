import numpy as np
from keras.models import Model, load_model
import keras.backend as K
netModel = load_model("netmodel.h5")
xx = list(map(int, input("Enter Age, Speciality(0-2500), International Reputation(0-5), Skill Moves(0-5), Work Rate(0-5), Position(0=GK, 4=forward), Ability(0-200):\n").split()))
xx = np.array([xx])
result = netModel.predict(xx)
print("Market Value = ",result[0][0])
print("Wage = ", result[0][1])
