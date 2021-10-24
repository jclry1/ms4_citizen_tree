
[Back to README](../README.md#design---database)

The donation app uses two models with a foreign key link between them:


![Donations Models](/docs/readme_images/donations_models_fk.png)


At the moment, there is only one donation type ('Regular') with three price levels corresponding to three stripe IDs.
![Stripe Prices](/docs/readme_images/stripe_donation.png)