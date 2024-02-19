import random
import copy
import math
'''business 1, its the code from problem 1 but added cofifdence interval'''
def business1():
    def sample_mean(sample):
        '''does the value for the mean via finding the sum of all samples found in the sample_size '''
        return sum(sample) / len(sample) if len(sample) > 0 else 0  #returns the number of items in sample

    def sample_variance(sample):
        '''does the value for the variance via finding the sum of all samples found in the sample_size into an equation'''
        mean = sample_mean(sample)
        return sum((x - mean) ** 2 for x in sample) / len(sample) if len(sample) > 0 else 0  #returns the number of items in sample

    def confidence_interval(sample, confidence_level):
        '''Calculates the confidence interval for the mean'''
        mean = sample_mean(sample)
        sample_std = math.sqrt(sample_variance(sample))
        n = len(sample)
        if confidence_level == 0.95:
            z_critical = 1.80  # For a 95% confidence level for 11 tries
        else:
            raise ValueError("Unsupported confidence level")
        margin_of_error = z_critical * (sample_std / math.sqrt(n))
        return mean - margin_of_error, mean + margin_of_error
    def main():
        '''time to print everything, and the math, lots of math'''
        num_samples = 11 #how many times we want to fine a mean and variance.
        sample_size = 100 #how many rocks in each trial,
        samples = [] #starts the list to hold the values found.

        for _ in range(num_samples):
            rocks = [max(0, random.gauss(0.6875, 2.5)) for _ in range(sample_size)]
            '''according to my simple research, some gravel can be 10 inches in diameter to still be considered gravel, thus I threw in the chance 
            that the rocks could be 10 inches, however you can't have a negative rock so I put a max value'''
            sample = [rock for rock in rocks if 1 >= rock >= 3/8]  # Filter rocks between 1" and 3/8", anything outside this range just doesn't work
            samples.append(copy.deepcopy(sample)) #copys the number

        sample_means = [sample_mean(sample) for sample in samples] #repeats the for_in thing above till 100 samples have been collected, changing the numper each time.
        #goes back the sample_mean funtion to put the number found, getting a number, and repeating everything until we have 11 samples
        sample_variances = [sample_variance(sample) for sample in samples] #repeats the for_in thing above till 100 samples have been collected, changing the number each time
        # goes back the sample_variance funtion to put the number found, getting a number, and repeating everything until we have 11 samples
        print("Sample Mean and Variance of each sample:")
        for i in range(num_samples):
            print(f"Sample {i+1}: Mean = {sample_means[i]}, Variance = {sample_variances[i]}")
            '''does this for each of the 11 samples, just so we can see the numbers and trouble shoot'''

        print("\nMean and Variance of the sampling mean:")
        mean_of_means = sum(sample_means) / num_samples
        '''gets the sum of all sample means divided by 11 so we can get well, the mean of everything'''
        variance_of_means = sum(sample_variances)/ num_samples
        '''gets the sum of all sammple_variance_of_means divided by 11 so we can get well, the mean of everything'''
        print(f"Mean of Sampling Mean: {mean_of_means}")
        print(f"Variance of Sampling Mean: {variance_of_means}")

        '''so i have no clue what is being asked, i'm assuming the confidence interval. so this is the confidence interval for business 1
         had to use chatgpt as most examples used scipy or numbpy'''
        confidence_level = 0.95  # 95% confidence level
        lower, upper = confidence_interval(sample_means, confidence_level)
        print(f"Confidence Interval for the Mean (at {confidence_level * 100}% confidence level):")
        print(f"Lower Bound: {lower}")
        print(f"Upper Bound: {upper}")


    if __name__ == "__main__":
        main()
'''business 2, its the code from problem 1 but modfidied to have 7/8 added cofifdence interval'''
def business2():
    def sample_mean(sample):
        '''does the value for the mean via finding the sum of all samples found in the sample_size '''
        return sum(sample) / len(sample) if len(sample) > 0 else 0  #returns the number of items in sample

    def sample_variance(sample):
        '''does the value for the variance via finding the sum of all samples found in the sample_size into an equation'''
        mean = sample_mean(sample)
        return sum((x - mean) ** 2 for x in sample) / len(sample) if len(sample) > 0 else 0  #returns the number of items in sample
    def confidence_interval(sample, confidence_level):
        '''Calculates the confidence interval for the mean'''
        mean = sample_mean(sample)
        sample_std = math.sqrt(sample_variance(sample))
        n = len(sample)
        if confidence_level == 0.95:
            z_critical = 1.80  # For a 95% confidence level for 11 tries
        else:
            raise ValueError("Unsupported confidence level")
        margin_of_error = z_critical * (sample_std / math.sqrt(n))
        return mean - margin_of_error, mean + margin_of_error
    def main():
        '''time to print everything, and the math, lots of math'''
        num_samples = 11 #how many times we want to fine a mean and variance.
        sample_size = 100 #how many rocks in each trial,
        samples = [] #starts the list to hold the values found.

        for _ in range(num_samples):
            rocks = [max(0, random.gauss(0.625, 2.5)) for _ in range(sample_size)]
            '''according to my simple research, some gravel can be 10 inches in diameter to still be considered gravel, thus I threw in the chance 
            that the rocks could be 10 inches, however you can't have a negative rock so I put a max value'''
            sample = [rock for rock in rocks if 7/8 >= rock >= 3/8]  # Filter rocks between 1" and 3/8", anything outside this range just doesn't work
            samples.append(copy.deepcopy(sample)) #copys the number

        sample_means = [sample_mean(sample) for sample in samples]
        '''repeats the for_in thing above till 100 samples have been collected, changing the numper each time.
        goes back the sample_mean funtion to put the number found, getting a number, and repeating everything until we have 11 samples'''
        sample_variances = [sample_variance(sample) for sample in samples]
        '''repeats the for_in thing above till 100 samples have been collected, changing the number each time
        # goes back the sample_variance funtion to put the number found, getting a number, and repeating everything until we have 11 samples'''
        print("Sample Mean and Variance of each sample:")
        for i in range(num_samples):
            print(f"Sample {i+1}: Mean = {sample_means[i]}, Variance = {sample_variances[i]}")
            '''does this for each of the 11 samples, just so we can see the numbers and trouble shoot'''

        print("\nMean and Variance of the sampling mean:")
        mean_of_means = sum(sample_means) / num_samples
        '''gets the sum of all sample means divided by 11 so we can get well, the mean of everything'''
        variance_of_means = sum(sample_variances)/ num_samples
        '''gets the sum of all sammple_variance_of_means divided by 11 so we can get well, the mean of everything'''
        print(f"Mean of Sampling Mean: {mean_of_means}")
        print(f"Variance of Sampling Mean: {variance_of_means}")

        '''so i have no clue what is being asked, i'm assuming the confidence interval. so this is the confidence interval for business 2 
        had to use chatgpt as most examples i found online were using scipy or numpy'''
        confidence_level = 0.95  # 95% confidence level
        lower, upper = confidence_interval(sample_means, confidence_level)
        print(f"Confidence Interval for the Mean (at {confidence_level * 100}% confidence level):")
        print(f"Lower Bound: {lower}")
        print(f"Upper Bound: {upper}")



    if __name__ == "__main__":
        main()
'''prints business 1 and 2'''
business1()
business2()
'''my code is very messy and i could not get the values to leave. i tried with chatgpt to get
it to do it but it broke my code because it tried to "simplfy" my code so i just left it as a 
mess and said the following'''
print('on averge, business 1 has bigger gravel and buisness 2 has finer gravel')