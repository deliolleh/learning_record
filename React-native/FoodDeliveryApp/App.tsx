import * as React from 'react';
import {NavigationContainer, ParamListBase} from '@react-navigation/native';
import {
  createNativeStackNavigator,
  NativeStackScreenProps,
} from '@react-navigation/native-stack';
import {Pressable, Text, TouchableHighlight, View} from 'react-native';
import {useCallback} from 'react';

type RootStackParamList = {
  Home: undefined;
  Details: undefined;
};
type HomeScreenProps = NativeStackScreenProps<RootStackParamList, 'Home'>;
type DetailsScreenProps = NativeStackScreenProps<ParamListBase, 'Details'>;

function HomeScreen({navigation}: HomeScreenProps) {
  const onClick = useCallback(() => {
    navigation.navigate('Details');
  }, [navigation]);

  return (
    <>
      <View style={{flex: 1, backgroundColor: 'yellow', alignItems: 'center', justifyContent: 'center'}}>
        <Pressable onPress={onClick} style={{ padding: 20, backgroundColor: 'blue' }}>
          {/* TouchableHighlight는 ios에서는 없는 것 같다 Pressable은 and/ios 가리지 않는듯 */}
          {/*
            padding/margin을 Web에서는 '0 0 0 0' 형식으로 shortcut할 수 있지만 native는 paddingLeft 등 일일이 지정해야한다
            단 좌우 => Horizontal, 상하 => Vertical으로 합칠 수는 있음
          */}
          <Text style={{ color: 'white' }}>Go Detail</Text>
          {/* react-native는 div 안의 text style을 div에서 처리하지 못하고 text에서 direct하게 입력해야한다 */}
        </Pressable>
      </View>
      <View style={{flex: 2, backgroundColor: 'green', alignItems: 'flex-end', justifyContent: 'center'}}><Text>Second Screen</Text></View>
    </>
  );
}

function DetailsScreen({navigation}: DetailsScreenProps) {
  const onClick = useCallback(() => {
    navigation.navigate('Home');
  }, [navigation]);

  return (
          <View style={{flex: 1, alignItems: 'center', justifyContent: 'center'}}>
            <TouchableHighlight onPress={onClick}>
              <Text>Details Screen</Text>
            </TouchableHighlight>
          </View>
  );
}

const Stack = createNativeStackNavigator();
function App() {
  return (
          <NavigationContainer>
            <Stack.Navigator initialRouteName="Home">
              <Stack.Screen
                      name="Home"
                      component={HomeScreen}
                      options={{title: 'Home'}}
              />
              <Stack.Screen name="Details">
                {props => <DetailsScreen {...props} />}
              </Stack.Screen>
            </Stack.Navigator>
          </NavigationContainer>
  );
}

export default App;