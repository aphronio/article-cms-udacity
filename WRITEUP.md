# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.

*For **both** a VM or App Service solution for the CMS app:*
- *Analyze costs, scalability, availability, and workflow*
- *Choose the appropriate solution (VM or App Service) for deploying the app*
- *Justify your choice*

APP Service is cost effective in the sense that it is optimized for the app if it is supported by azure and most low level things are handled by azure so developer can focus on code logic. Workflow for App service is also very straightforward as azure supports Continous integration with the code base using github actions. VM would also be scalable easily but workflow would be a bit more complex and user would need to deal with additional costs if its not set up efficiently.

I chose App service for this app because it is simple python app which is already supported by azure app services. And for this app I didn't need any system level controls so increasing the complexity by choosing a VM didn't make much sense.
### Assess app changes that would change your decision.

*Detail how the app and any other needs would have to change for you to change your decision in the last section.* 

If the app had been more complex and required system level controls for example in case of security or operating system level optimizations. Or even the code base consisted of different mix of languages not supported by azure. Then I would go for a VM for more low level control and finetuning.