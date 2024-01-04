import React from "react";
import { View, StyleSheet } from "react-native";
import { COLORS } from '../constants/colors'

export default function Login() {
    return (
        <View style={styles.container}>
            <h1>Login</h1>
        </View>
    )
};

// styles
const styles = StyleSheet.create({
    container: {
      flex: 1,
      backgroundColor: COLORS.lightgray,
      alignItems: 'center',
      justifyContent: 'center',
    },
  });