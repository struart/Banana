#!/usr/bin/env python
# Sample script to show how to send SM

import I2C_LCD_driver
import time
import smbus
import sqlite3 as lite

#def main():
I2C_LCD_driver.LCD_NOC = 1
mylcd = I2C_LCD_driver.lcd()
while True:
 mylcd.lcd_display_string("Godzina: %s" %time.strftime("%H:%M"), 2)
 mylcd.lcd_display_string("Data: %s" %time.strftime("%m/%d/%Y"), 3)
# mylcd.backlight(1)
 time.sleep(20)
 try:
  con = lite.connect('/var/www/html/banan_baza.db')
  cur = con.cursor()
  cur.execute("SELECT * FROM phones")
  rows = cur.fetchall()
  for row in rows:
   sygnal = str(row[12])
   siec = str(row[9])
   nadajnik = str(row[8])
 except lite.Error, e:
  print "Error %s:" % e.args[0]
  sys.exit(1)
 finally:
  if con:
   con.close()
 mylcd.lcd_clear()
 mylcd.lcd_display_string("Status modemu GSM", 1)
 mylcd.lcd_display_string("Siec: %s" %siec, 2)
 mylcd.lcd_display_string("Sygnal: -%s" %sygnal, 3)
 mylcd.lcd_display_string("ID: %s" %nadajnik, 4)
 #mylcd.backlight(1)
 time.sleep(20)
 mylcd.lcd_clear()
