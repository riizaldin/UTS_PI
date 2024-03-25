class BMI:
    def __init__(self, weight_lb, height_ft):
        self.weight_lb = weight_lb
        self.height_ft = height_ft
    
    @property
    def Weight(self):
        return self.weight_lb
    
    @property
    def Height(self):
        return self.height_ft
    
    def BMI_Value(self):
        weight_lb = self.weight_lb * 0.453592
 
        height_ft = self.height_ft * 0.3048
        
        return weight_lb / (height_ft ** 2)
    
    def __eq__(self, other):
        if isinstance(other, BMI):
            return self.weight_lb == other.weight_lb and self.height_ft == other.height_ft
        return False

person1 = BMI(weight_lb=109.4, height_ft=5.4)
person2 = BMI(weight_lb=109.4, height_ft=5.4)

print("BMI dari orang 1:", person1.BMI_Value())
print("BMI dari orang 2:", person2.BMI_Value())

print("Apakah orang 1 dan 2 sama?", person1 == person2)
