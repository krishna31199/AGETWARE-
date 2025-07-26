# ShopHub - E-commerce Product Dashboard

A modern, responsive e-commerce product dashboard built with React, TypeScript, and Tailwind CSS. Features product browsing, detailed views, shopping cart functionality, and simulated checkout process.

## 🚀 Features

### Core Functionality
- **Product Browsing**: Grid view of products with search and filtering capabilities
- **Product Details**: Comprehensive product information with high-quality presentation
- **Shopping Cart**: Full CRUD operations (add, update quantity, remove items)
- **Simulated Checkout**: Mock checkout process with order confirmation
- **Responsive Design**: Optimized for mobile, tablet, and desktop devices

### Advanced Features
- **Real-time Search**: Filter products by name or category
- **Smart Filtering**: Sort by price, rating, and name
- **State Management**: React Context API for cart state
- **Loading States**: Skeleton screens and loading indicators
- **Error Handling**: Graceful error states with retry functionality
- **Animations**: Smooth transitions and micro-interactions

## 🛠️ Technology Stack

- **Frontend**: React 18, TypeScript
- **Routing**: React Router DOM
- **Styling**: Tailwind CSS
- **Icons**: Lucide React
- **API**: Fake Store API for product data
- **State Management**: React Context API + useReducer
- **Build Tool**: Vite

## 📁 Project Structure

```
src/
├── components/
│   ├── common/
│   │   ├── Header.tsx          # Navigation header with cart indicator
│   │   ├── Loading.tsx         # Loading components and skeletons
│   │   └── SearchBar.tsx       # Reusable search input
│   ├── product/
│   │   ├── ProductCard.tsx     # Individual product card
│   │   ├── ProductGrid.tsx     # Product grid layout
│   │   └── ProductFilters.tsx  # Category and sort filters
│   └── cart/
│       ├── CartItem.tsx        # Individual cart item
│       └── CartSummary.tsx     # Order summary and checkout
├── pages/
│   ├── HomePage.tsx            # Main product listing page
│   ├── ProductDetailPage.tsx   # Detailed product view
│   └── CartPage.tsx            # Shopping cart page
├── contexts/
│   └── CartContext.tsx         # Cart state management
├── hooks/
│   └── useProducts.ts          # Product data fetching hooks
├── types/
│   └── product.ts              # TypeScript type definitions
├── utils/
│   └── api.ts                  # API utility functions
└── App.tsx                     # Main application component
```

## 🎨 Design System

### Color Palette
- **Primary**: Blue (#3B82F6) - Main brand color
- **Secondary**: Emerald (#10B981) - Success states
- **Accent**: Amber (#F59E0B) - Highlights and warnings
- **Neutrals**: Gray scale for text and backgrounds

### Typography
- **Headings**: Bold, clear hierarchy
- **Body**: Readable, accessible contrast ratios
- **Interactive**: Hover states and feedback

### Layout
- **Mobile-first**: Responsive breakpoints
- **Grid System**: CSS Grid and Flexbox
- **Spacing**: Consistent 8px spacing system

## 🚀 Getting Started

### Prerequisites
- Node.js (version 16 or higher)
- npm or yarn package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd shophub
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Start the development server**
   ```bash
   npm run dev
   ```

4. **Open your browser**
   Navigate to `http://localhost:5173`

### Build for Production

```bash
npm run build
```

The build artifacts will be stored in the `dist/` directory.

## 📱 Usage

### Browsing Products
1. View products on the home page in a responsive grid layout
2. Use the search bar to find specific products
3. Filter by category or sort by price/rating
4. Click on any product card to view details

### Product Details
1. View comprehensive product information
2. See high-quality product images
3. Read detailed descriptions and ratings
4. Add items to your cart with one click

### Shopping Cart
1. View all items in your cart
2. Update quantities with +/- buttons
3. Remove items with the trash icon
4. See real-time price calculations
5. Proceed to simulated checkout

### Checkout Process
1. Review order summary with totals
2. See shipping and tax calculations
3. Click "Proceed to Checkout" for simulation
4. Receive order confirmation

## 🔧 API Integration

The application uses the [Fake Store API](https://fakestoreapi.com/) for product data:

- **GET /products** - Fetch all products
- **GET /products/:id** - Fetch single product
- **GET /products/categories** - Fetch product categories

## 🧪 Testing

Run the test suite:
```bash
npm run test
```

## 🚀 Deployment

The application can be deployed to various platforms:

### Vercel
```bash
npm run build
# Deploy to Vercel
```

### Netlify
```bash
npm run build
# Upload dist/ folder to Netlify
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- [Fake Store API](https://fakestoreapi.com/) for providing product data
- [Lucide React](https://lucide.dev/) for beautiful icons
- [Tailwind CSS](https://tailwindcss.com/) for utility-first styling
- [React](https://reactjs.org/) for the amazing framework

---

Built with ❤️ by [Your Name]# Front-end
