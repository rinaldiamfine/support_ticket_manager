import React from "react";

import { Text, View, FlatList, StyleSheet } from 'react-native';
import { styled } from 'nativewind';

const StyledView = styled(View);
const StyledText = styled(Text);
const StyledFlatList = styled(FlatList);
const SidebarData = [
    {
        id: '1',
        title: 'Dashboards',
    },
    {
        id: '2',
        title: 'Tickets',
    },
    {
        id: '3',
        title: 'Accounts',
    },
    {
        id: '4',
        title: 'Settings',
    },
];
const styles = StyleSheet.create({
    container: {
      backgroundColor: '#fff',
      alignItems: 'left',
      justifyContent: 'center',
    },
});
const Item = ({title}) => (
    <StyledView style={styles.item}>
        <StyledText style={styles.title}>{title}</StyledText>
    </StyledView>
);

export default function Sidebar() {
    return (
    <StyledFlatList
        data={SidebarData}
        renderItem={({item}) => <Item title={item.title} />}
        keyExtractor={item => item.id}
    />
    )
};