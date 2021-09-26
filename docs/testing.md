# Testing for MS3 <!-- omit in toc -->
The testing oultined below is organised by user stories (US) (individually or grouped).
Note: Testing is ongoing with final changes to the appearance of the site. Some of the screenshots may not match exactly with the submitted version in terms of the appearance.

## Tests For First-Time or Non-Registered User

### As a first-time visitor, the purpose and overall content of the site is clear and easy to navigate
Steps:
1. Navigate to the site and asses whether the purpose of the site is clearly evident and/or accessible to a non-registered user.

Result: Pass
When I navigate to the site, the image, heading, sub-heading are all consistent.
I can easily access the 'About' page from the landing page and this clearly outlines the site purpose.
I can also easil visit and use the calculator functinality and this illustrates with a meaningful and unique-to-me exampleo f how  donation might help to store carbon and offset personal lifetyle emissions.

### The site appears and trustworthy
Steps:
1. Check the About page and the Calculator page to assess trustworthiness. Both should make it clear that the claims for sequestration/offsets are based on reliable data. Verify that the site does not actively request any payments or card data - in fact the user cannot donate without becoming a registered user.

Result: Pass 
When I navigate to the mentioned pages, resources are mentioned and I can verify that these exist.

### The calculator feature works
1. As a non-registered or non-logged-in user, attempt use the calculator function and check that the sequestration potential per 50 euro donation is calculated based on my input.
   
Result: Pass
The calculator page is accessible and the calculations update in line with my inputs. The 'sequestration potential' table updates dynamically with my input: Add screenshot here

### Access to site content is limited as non-logged in user, encouraging registration
1. Navigate to the site and attempt to access the 'Projects' or 'Donate' pages. Verify that this is not p[ossible while user is not logged in.

Result: Pass.
Having established the basic credibility of the site, the user attempts to view the projects (and associated updates) or make a donation. however, they must log in, prompting user registration.


## Tests For Non-Contributing User
### I can make a donation and this is verified by email
1. Register and log in to the site.
2. Verify that the content that was available when not logged in is still accessible.
3. Click the Donate button from one of the locations in which it appears.
4. Verify that you have 3 donate options - 20 euros, 50 euros, 100 euros.
5. Select an amount to donate.
6. Verify that the Stripe checkout opens and the selected amount is displayed as the amount to pay.
7. Enter card details (use Stripe test card 4242 4242 4242 4242, with future expiry and any 3-digit combination for CVV).
8. Verify that the stripe presents a successful message and you are directed to a success page on Citizen Tree.
9. Confirm that an email is received confirming the donation and has the correct amount.

Pass: All steps above complete.

### I can access project and project updates content but cannot edit
1. 