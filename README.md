Description of E-commerce Dashboard

![WhatsApp Image 2025-07-26 at 14 18 28_24d78f1f](https://github.com/user-attachments/assets/c48d5607-a083-4fd2-b97a-9ecc89fce15d)
![WhatsApp Image 2025-07-26 at 14 18 28_ebab126d](https://github.com/user-attachments/assets/55db37e8-f29a-46ea-ae1a-3ebdcf1fb0c8)
![WhatsApp Image 2025-07-26 at 14 18 28_574e334b](https://github.com/user-attachments/assets/04191b79-763e-482c-8c1b-a4cd6f73cbcc)
![WhatsApp Image 2025-07-26 at 14 18 29_93754db9](https://github.com/user-attachments/assets/9af01984-9afa-4176-b772-0de338d2e1d0)
![WhatsApp Image 2025-07-26 at 14 18 29_a3620edf](https://github.com/user-attachments/assets/c303719d-5ab1-4018-9df3-76c7cd5ea649)
![WhatsApp Image 2025-07-26 at 14 18 29_c8b4fb2b](https://github.com/user-attachments/assets/7bdd25c3-8cc9-42ab-8c75-863d8a8a3818)

This file defines the main structure of your React application. Here’s what it does:
Imports:
React and routing components from react-router-dom.
Context provider for the shopping cart (CartProvider).
Common UI components like Header.
Page components: HomePage, ProductDetailPage, and CartPage.
App Component:
Wraps the entire app in a CartProvider so that cart state is available throughout the app.
Uses BrowserRouter (Router) to enable client-side routing.
Renders a Header at the top of every page.
Defines three main routes:
/ → Home page (product listing or landing page)
/product/:id → Product detail page (shows details for a specific product)
/cart → Shopping cart page
Styling:
The main container uses Tailwind CSS classes for a minimum screen height and background color.
Export:
Exports the App component as the default export.
