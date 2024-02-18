import { useFonts } from "expo-font";
import { SplashScreen, Stack } from "expo-router";
import {useEffect} from "react";

export const unstable_settings = {
  initialRouteName: "(tabs)",
};

// Prevent the splash screen from auto-hiding before asset loading is complete.
SplashScreen.preventAutoHideAsync();

export default function RootLayout() {
  const [loaded, error] = useFonts({
    "prompt-900": require("../assets/fonts/Prompt-Black.ttf"),
    "prompt-800": require("../assets/fonts/Prompt-ExtraBold.ttf"),
    "prompt-700": require("../assets/fonts/Prompt-Bold.ttf"),
    "prompt-600": require("../assets/fonts/Prompt-SemiBold.ttf"),
    "prompt-500": require("../assets/fonts/Prompt-Medium.ttf"),
    "prompt-400": require("../assets/fonts/Prompt-Regular.ttf"),
    "prompt-300": require("../assets/fonts/Prompt-Light.ttf"),
    "prompt-200": require("../assets/fonts/Prompt-ExtraLight.ttf"),
    "prompt-100": require("../assets/fonts/Prompt-Thin.ttf"),
  });
   // Expo Router uses Error Boundaries to catch errors in the navigation tree.
  useEffect(() => {
    if (error) throw error;
  }, [error]);

  useEffect(() => {
    if (loaded) {
      SplashScreen.hideAsync();
    }
  }, [loaded]);

  if (!loaded) {
    return null;
  }

  return(<RootLayoutNav />)
}

function RootLayoutNav() {
  return (
    <Stack>
      <Stack.Screen name="(tabs)" options={{headerShown: false}} />
    </Stack>
  );
}
