// Abstract base class (or interface-like structure)
class PaymentMethod {
    process(amount) {
      throw new Error("process() must be implemented");
    }
  }
  
  // Individual payment method classes
  class CreditCardPayment extends PaymentMethod {
    process(amount) {
      console.log(`Processing credit card payment of $${amount}`);
    }
  }
  
  class PayPalPayment extends PaymentMethod {
    process(amount) {
      console.log(`Processing PayPal payment of $${amount}`);
    }
  }
  
  class BankTransferPayment extends PaymentMethod {
    process(amount) {
      console.log(`Processing bank transfer payment of $${amount}`);
    }
  }
  
  // Payment Processor
  class PaymentProcessor {
    processPayment(paymentMethod, amount) {
      paymentMethod.process(amount);
    }
  }
  
  // Usage
  const paymentProcessor = new PaymentProcessor();
  paymentProcessor.processPayment(new CreditCardPayment(), 100);
  paymentProcessor.processPayment(new PayPalPayment(), 200);
  paymentProcessor.processPayment(new BankTransferPayment(), 300);
  
  // Adding a new payment method (e.g., CryptoPayment)
  class CryptoPayment extends PaymentMethod {
    process(amount) {
      console.log(`Processing crypto payment of $${amount}`);
    }
  }
  
  // Now, you can use it without modifying the PaymentProcessor
  paymentProcessor.processPayment(new CryptoPayment(), 500);
  