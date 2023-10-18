# CDK Workshop at Imperial College London

We assume that you have the AWS CLI installed. If you don't, install it [here](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html). We also assume that you have an AWS account set up.    

You'll also need Node and Python installed.  

## What is CDK?

![image](/assets/AppStacks.png)

The AWS CDK lets you build reliable, scalable, cost-effective applications in the cloud with the considerable expressive power of a programming language. This approach yields many benefits, including:

- Build with high-level constructs that automatically provide sensible, secure defaults for your AWS resources, defining more infrastructure with less code.

- Use programming idioms like parameters, conditionals, loops, composition, and inheritance to model your system design from building blocks provided by AWS and others.

- Put your infrastructure, application code, and configuration all in one place, ensuring that at every milestone you have a complete, cloud-deployable system.

- Employ software engineering practices such as code reviews, unit tests, and source control to make your infrastructure more robust.

- Connect your AWS resources together (even across stacks) and grant permissions using simple, intent-oriented APIs.

- Import existing AWS CloudFormation templates to give your resources a CDK API.

- Use the power of AWS CloudFormation to perform infrastructure deployments predictably and repeatedly, with rollback on error.

- Easily share infrastructure design patterns among teams within your organization or even with the public.

The AWS CDK supports TypeScript, JavaScript, Python, Java, C#/.Net, and Go. Developers can use one of these supported programming languages to define reusable cloud components known as Constructs. You compose these together into Stacks and Apps.  

## Installing CDK

`npm install -g aws-cdk`  

We install CDK with the Node Package Manager. The AWS CDK Toolkit, the CLI command `cdk`, is the primary tool for interacting with your AWS CDK app. It executes your app, interrogates the application model you defined, and produces and deploys the AWS CloudFormation templates generated by the AWS CDK. It also provides other features useful for creating and working with AWS CDK projects.  

## Commands to Know

### Bootstrapping

`cdk bootstrap`  

**Bootstrapping** is the process of provisioning resources for the AWS CDK before you can deploy AWS CDK apps into an AWS environment. (An AWS environment is a combination of an AWS account and Region).  

These resources include an Amazon S3 bucket for storing files and IAM roles that grant permissions needed to perform deployments.  

The required resources are defined in an AWS CloudFormation stack, called the bootstrap stack, which is usually named CDKToolkit. Like any AWS CloudFormation stack, it appears in the AWS CloudFormation console once it has been deployed.  

### Synthesis

`cdk synth`  

**Synthesis** - AWS CDK apps are effectively only a definition of your infrastructure using code. When CDK apps are executed, they produce (or “synthesize”, in CDK parlance) an AWS CloudFormation template for each stack defined in your application.  

### Deployment and Destruction

`cdk deploy`  

Deploys one or more specified stacks.  

`cdk destroy`  
	
Destroys one or more specified stacks.  

`cdk watch`

Monitors your code and assets for changes and attempts to perform a deployment automatically when a change is detected.  

### Listing

`cdk ls`  

Lists the stacks in the app.  

## What we are Building

In this repository, we are going to demonstrate the use of CDK to build a simple webservice, consisting of API Gateway, Lambda and DynamoDB. This is a common pattern in serverless appliactions.  

The code we use here describes the creation of a Construct `HitCounter` which can be attached to any Lambda function that is used as an API Gateway Backend. It is used to count how many requests we issue to each URL path and then store this in a DynamoDB table.  

![image](/assets/hit-counter.png)

