import { StatusBar } from 'expo-status-bar';
import React from 'react';
// @ts-ignore
import { StyleSheet, Text, View } from 'react-native';
import TcpSocket from 'react-native-tcp-socket'
export default function App() {

  const options = {host: "google.com", port: 443, tls: true}

  // Create socket
  const client = TcpSocket.createConnection(options, () => {
    // Write on the socket
    client.write('Hello server!');

    // Close socket
    client.destroy();
  });

  return (
    <View style={styles.container}>
      <Text>Open up App.tsx to start working on your app!</Text>
      <StatusBar style="auto" />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
