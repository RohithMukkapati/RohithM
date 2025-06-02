
WeatherTrack is a simple Android app built using Java and MVVM architecture. It tracks daily weather data using a mock API, stores the data locally every 6 hours using WorkManager, and displays a weekly summary with temperature trends.


Features

- Fetches temperature, humidity, and weather condition from a mock JSON file.
- Saves records to local Room DB every 6 hours via WorkManager.
- Users can manually refresh weather data.
- Weekly summary screen with temperature trend graph and detail view per day.
- Error handling for no internet/API issues/DB errors.

---

Requirements

- JDK 11 or higher
- Android SDK (install via Android Studio)
- AVD Emulator or physical Android device connected via USB with USB Debugging enabled
- Visual Studio Code with Java and Android extensions installed

---

Setup Instructions (VS Code)

1.Open the Project

Extract the project ZIP or clone the repo, then open the root `WeatherTrack` folder in VS Code.

```bash
cd path/to/WeatherTrack
```

---

2. Build the Project

Run Gradle wrapper to build the app:

```bash
./gradlew build         # macOS/Linux
gradlew.bat build       # Windows
```

---

3. Start Android Emulator or Connect Device

- Start an Android emulator via Android Studio or command line:

```bash
emulator -avd <your_emulator_name>
```

- Or connect a physical Android device with **USB Debugging** enabled.

Verify connection with:

```bash
adb devices
```

Your device or emulator should be listed.

---

4. Install the App

Install the debug build to your device or emulator:

```bash
./gradlew installDebug         # macOS/Linux
gradlew.bat installDebug       # Windows
```

---

5. Launch the App

Open the  WeatherTrack app on your device/emulator.

---

App Usage

- The app automatically fetches weather data every 6 hours in the background.
- Use the Refresh button to manually fetch and save weather data.
- View the weekly summary graph to see temperature trends.
- Tap any day on the summary to view detailed weather stats.

