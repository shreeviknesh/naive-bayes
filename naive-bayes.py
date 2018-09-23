def calculateTotalProb(dataset):
	#Total probability of getting YES and NO
	global totalPositive
	global totalNegative

	positive, negative = 0, 0

	for instance in dataset:
		if instance[-1] == 'yes':
			positive += 1
		else:
			negative += 1

	totalPositive, totalNegative = positive / (positive + negative), negative / (positive + negative)

def conditionalProbAttribute(pos, attribute, dataset):
	yesPositive, yesNegative = 0, 0
	noPositive, noNegative = 0, 0

	for instance in dataset:
		if instance[-1] == 'yes':
			if instance[pos] == attribute:
				yesPositive += 1
			else:
				yesNegative += 1
		else:
			if instance[pos] == attribute:
				noPositive += 1
			else:
				noNegative += 1

	conditionalYes = yesPositive / (yesPositive + yesNegative)
	conditionalNo = noPositive / (noPositive + noNegative)

	return conditionalYes, conditionalNo

def naiveBayesPredict(instance, dataset):
	calculateTotalProb(dataset)
	positive, negative = 1, 1

	#Traverse through all the attributes
	for pos in range(0, len(instance)):
		yes, no = conditionalProbAttribute(pos, instance[pos], dataset)
		positive *= yes
		negative *= no

	#Normalizing the values [not necessary]
	temp = positive
	positive = temp / (temp + negative)
	negative = negative / (temp + negative)

	#If YES is more probable than NO
	if positive >= negative:
		prediction = "yes"
	else :
		prediction = "no"

	#All the probabilities
	#print(positive, negative, prediction)

	return prediction

def calculateAccuracy(training, test):
	#The number of correct and wrong predictions
	correct, wrong = 0, 0

	#Traversing through all the instances in test dataset to predict
	for instance in test:
		prediction = naiveBayesPredict(instance[0: -1], training)

		#Checking if the prediction is correct or wrong
		if prediction == instance[-1]:
			correct += 1
		else:
			wrong += 1

	#ACCURACY
	return correct / (correct + wrong)

if __name__ == '__main__':
	from dataset import *
	print("Accuracy of model:", calculateAccuracy(trainingData, testData))