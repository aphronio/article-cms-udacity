# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.

*For **both** a VM or App Service solution for the CMS app:*
- *Analyze costs, scalability, availability, and workflow*
- *Choose the appropriate solution (VM or App Service) for deploying the app*
- *Justify your choice*

### Answer
- - By using the pricing calculator of Azure, I found out that the plans available for App Service are cheaper as compared to the VM. Because in APP service I could start with free plan to test things out which is the case with this project and even later on I could move to a shared plan for low traffic website which would still be cheaper than the lowest cost plan available(Basic) in VM for my region. 
  - App service also offers built in auto vertical scaling with integrated load balancer as opposed to the VM scale sets which are more geared towards horizontal scaling.
  - In terms of availalbility both VM and app service offer > 99% availability for premium plans but for starting out basic plan of App service offers 99.95% availability gaurantee as compared to 95% availability gaurantee offered by a single VM in basic plan with standard HDD.
  - Workflow is much more straightforward and smoother for APP Service with built in CI, easy deployment and even with the flexibilty of scheduling jobs via WebJobs. VM offers more flexibility to interact with running system but in terms of CI/CD one needs to set this up manually.

- APP Service is cost effective in the sense that it is optimized for the app if it is supported by azure and most low level things are handled by azure so developer can focus on code logic. It is also cheaper than opting for a VM for our use case. Workflow for App service is also very straightforward as azure supports Continous integration with the code base using github actions. VM would also be scalable easily but workflow would be a bit more complex and user would need to deal with additional costs if its not set up efficiently.

- I chose App service for this app because it is simple python app which is already supported by azure app services. It is cheaper in terms of pricing, workflow is easier, and for this app I didn't need any system level controls and access to server so increasing the complexity by choosing a VM didn't make much sense.
### Assess app changes that would change your decision.

*Detail how the app and any other needs would have to change for you to change your decision in the last section.* 

### Answer
- If the app had been more complex and required system level controls for example in case of security or operating system level optimizations. 
- If i think that in future the technology stack could change or even if the current code base consisted of different mix of languages not supported by azure. 
- The pricing for VM is better if I need more disk space and more performance in future.
- If I need access to server beyond running webjobs to track.

Then I would go for a VM for more low level control and finetuning.