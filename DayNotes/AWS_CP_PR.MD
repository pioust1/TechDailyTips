# AWS Cloud Practitioner Practice
1. ## AWS Billing  
        Configure how to set budgets in the billing dashboard  
	Budgets can be made either on the basis of usage or cost. We can set the minimum threshold value of the total amount incurred.  
	It can also set budgets on the bas of RI utlizations  which can track any under or over utlizations.
	Once set we can configure billing alarms whenever there is a breach in the threshold set.Once it is set we can have a notfication sent to our configured email.
2. ## IAM : [*Identity and Access Management*](https://docs.aws.amazon.com/iam/)   
   You must create a separate account for yourself use that instead of the root account. It is  best practice to create a user attached to a group.
   Refer the below snapshot to see how to create a user and the group.
  
   ### IAM Best practice  
      Never use the root user always use maintain other user for work.
      Always create groups , add policies to it with a good password policy
      MFA authentication is must for all users to guarantee it will be safe from hackers
      IAM roles can be attached ECE service as and when required. Basically to give permission to one AWS service to use another
      If AWS to be used programatically then create a AWS Access keys are just like pwd keep them safe
      IAM credential reports to check the user and their usage.
      Access Advisor :  to check how the user utlizes each of the services and the one which can be removed if there is no action done on it
   ### Shared responsibility model
   	What is AWS responsible for   
	 everything that they create : global infrastructure ; network ; overall security
	What is the user responsible for  
	  Creation of groups;users;policies;enabling MFA;Keys are rotated often;use IAM tools to add policies.  
   [IAM FAQ](https://aws.amazon.com/iam/faqs/)
3. ## EC2 [*EC2*](https://docs.aws.amazon.com/ec2/index.html)  
	

	
   
    
    

    	
