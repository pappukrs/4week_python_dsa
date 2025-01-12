import create from 'zustand';

// Create the store
const useStore = create((set) => ({
  count: 0,  // Initial state
  increase: () => set((state) => ({ count: state.count + 1 })),
  decrease: () => set((state) => ({ count: state.count - 1 })),
}));
