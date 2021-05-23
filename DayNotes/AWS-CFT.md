## AWS Cloudformation

Cloudformation deals with two things, one is templates and other is stacks. Ideally one creates a template which describes AWS services with their properties and stacks uses the same template to create AWS resources.  

* **TEMPLATES**  
   It is a JSON/YAML formatted text file,cloudformation uses these files as blueprints for building AWS resources.You can also specify multiple resources in a single template and    configure these resources to work together.CloudFormation templates have additional capabilities that you can use to build complex sets of resources and reuse those templates      in multiple contexts. For example, you can add input parameters whose values are specified when you create a CloudFormation stack. In other words, you can specify a value like    the instance type when you create a stack instead of when you create the template, making the template easier to reuse in different situations
* **STACKS**  
   All the resources created by the template are grouped in a single unit called a stack.You create, update, and delete a collection of resources by creating, updating, and          deleting stacks 
* **CHANGESETS**  
   If you need to make changes to the running resources in a stack, you update the stack. Before making changes to your resources, you can generate a change set, which is a          summary of your proposed changes. Change sets allow you to see how your changes might impact your running resources, especially for critical resources, before implementing them.
 ### HOW DOES CFT WORKS  
 When creating a stack, AWS CloudFormation makes underlying service calls to AWS to provision and configure your resources. CloudFormation can only perform actions that you have permission to do.
 
 Example:YAML, below template will create a EC2 instance with image id **as ami-0ff8a91507f77f867** and with instance type as **t1.micro**  
 
AWSTemplateFormatVersion: '2010-09-09'  
Description: A simple EC2 instance  
Resources:  
  MyEC2Instance:  
    Type: AWS::EC2::Instance  
    Properties:  
      ImageId: ami-0ff8a91507f77f867  
      InstanceType: t1.micro  
 
   
