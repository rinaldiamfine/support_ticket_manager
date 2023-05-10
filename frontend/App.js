import { StatusBar } from 'expo-status-bar';
import React from 'react';
import { Text, View, StyleSheet, FlatList } from 'react-native';
import { styled } from 'nativewind';
import Sidebar from './components/Sidebar';

const StyledView = styled(View);
const StyledText = styled(Text);
const StyledList = styled(FlatList);

const styles = StyleSheet.create({
  container: {
    flex: 1,
    flexDirection: 'row',
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});

export default function App() {
  return (
    <StyledView className="container h-12 justify-center bg-slate-300 items-center" style={styles.container}>
      <Sidebar></Sidebar>
      <Sidebar></Sidebar>
    </StyledView>
  );
}
