class my_calculator:

        def product(self, num1 = None, num2 = None, num3 = None):
                if num1 != None and num2 != None and num3 != None:
                        print(num1 * num2 * num3)
                elif num1 != None and num2 != None:
                        print(num1 * num2)
                else:
                        print(1 *num1)

        def product(self, *nums):
                print(nums)
                pro = 1
                for x in nums:
                        pro = pro * x
                print(pro)
       
#================================================================

c1 = my_calculator()
c1.product(4)
c1.product(4,5)
c1.product(4, 2, 2,4,5,6,7 ,7)
