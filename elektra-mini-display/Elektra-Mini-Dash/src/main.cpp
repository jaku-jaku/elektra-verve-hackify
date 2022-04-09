#include <Arduino.h>
#include "SPIFFS.h"
#include <TJpg_Decoder.h>
#include <SPI.h>
#include <TFT_eSPI.h> // Hardware-specific library

TFT_eSPI tft = TFT_eSPI(); // Invoke custom library
int imgNum = 0;

// $ pio run --target uploadfs
static bool tft_output(int16_t x, int16_t y, uint16_t w, uint16_t h, uint16_t *bitmap);
static void listSPIFFS(void);
void listAllFiles()
{

    File root = SPIFFS.open("/");

    File file = root.openNextFile();

    while (file)
    {

        Serial.print("FILE: ");
        Serial.println(file.name());

        file = root.openNextFile();
    }
}

void setup()
{
    Serial.begin(115200);

    // Initialise SPIFFS
    if (!SPIFFS.begin(true))
    {
        Serial.println("SPIFFS initialisation failed!");
        while (1)
            yield(); // Stay here twiddling thumbs waiting
    }
    Serial.println("\r\nInitialisation done.");
    listSPIFFS();

    tft.begin();
    tft.setRotation(0);
    tft.fillScreen(TFT_BLACK);

    TJpgDec.setJpgScale(1);
    TJpgDec.setSwapBytes(true);
    TJpgDec.setCallback(tft_output);

    // SPIFFS.remove("/mini-display.jpg");
    listAllFiles();
}

void loop()
{
    if (imgNum > 3)
        imgNum = 0;
    String imgPath = "/mini-display-";
    imgPath += imgNum++;
    imgPath += ".jpg";
    

    TJpgDec.drawFsJpg(0, 0, imgPath);
    delay(5000);
}

void listSPIFFS(void)
{
    Serial.println(F("\r\nListing SPIFFS files:"));
    static const char line[] PROGMEM = "=================================================";

    Serial.println(FPSTR(line));
    Serial.println(F("  File name                              Size"));
    Serial.println(FPSTR(line));

    fs::File root = SPIFFS.open("/");
    if (!root)
    {
        Serial.println(F("Failed to open directory"));
        return;
    }
    if (!root.isDirectory())
    {
        Serial.println(F("Not a directory"));
        return;
    }

    fs::File file = root.openNextFile();
    while (file)
    {

        if (file.isDirectory())
        {
            Serial.print("DIR : ");
            String fileName = file.name();
            Serial.print(fileName);
        }
        else
        {
            String fileName = file.name();
            Serial.print("  " + fileName);
            // File path can be 31 characters maximum in SPIFFS
            int spaces = 33 - fileName.length(); // Tabulate nicely
            if (spaces < 1)
                spaces = 1;
            while (spaces--)
                Serial.print(" ");
            String fileSize = (String)file.size();
            spaces = 10 - fileSize.length(); // Tabulate nicely
            if (spaces < 1)
                spaces = 1;
            while (spaces--)
                Serial.print(" ");
            Serial.println(fileSize + " bytes");
        }

        file = root.openNextFile();
    }

    Serial.println(FPSTR(line));
    Serial.println();
    delay(1000);
}

bool tft_output(int16_t x, int16_t y, uint16_t w, uint16_t h, uint16_t *bitmap)
{
    // Stop further decoding as image is running off bottom of screen
    if (y >= tft.height())
        return 0;

    // This function will clip the image block rendering automatically at the TFT boundaries
    tft.pushImage(x, y, w, h, bitmap);

    // Return 1 to decode next block
    return 1;
}
