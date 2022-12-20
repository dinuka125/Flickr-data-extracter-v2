import streamlit as st
import os
from telnetlib import STATUS
from tkinter.tix import Tree
import pandas as pd
from helper import date_checker1, df_creator, get_camera_info_thread, get_geo_info_thread, get_pic_thread, get_geo_info, get_camera_info,  out_dir, date_checker
from merge import merger
from shutil import rmtree

def scrapy(search_keyword,max_date,min_date):
    try:
        if search_keyword != '':
            dirpath = "./static"
            for filename in os.listdir(dirpath):
                filepath = os.path.join(dirpath, filename)
                try:
                    rmtree(filepath)
                    print("gabage removing")
                except OSError:
                    os.remove(filepath)
                    print("gabage removing")

            try:
                print(search_keyword , min_date , max_date)
                date_status = date_checker1(min_date, max_date)
                if date_status == True:
                    date_status2 = date_checker(min_date, max_date)
                    
                    if date_status2 == True:
                        get_pic_thread(search_keyword,min_date=min_date,max_date=max_date)
                        df_pic = pd.read_csv(out_dir +'/'+search_keyword+'_id.csv',sep=',')   
                        # df_creator(search_keyword)
                        get_camera_info_thread(search_keyword,df_pic)
                        get_geo_info_thread(search_keyword, df_pic)
                        merger(search_keyword)  
                        file = open("static"+"/"+search_keyword+"_Merged.csv") 
                        st.download_button(
                                            "Press to Download the Extracted data as CSV",
                                            file,
                                            "file.csv",
                                            "text/csv",
                                            key='download-csv'
                                            )
                    else:
                        st.error("Please re-check the date (min date should be greater than max date / two dates should not be the same date)")

                else:
                    st.error ("Please select valid date")           
                
                
            except Exception as e:
                st.error("Unxpected error ::", e)
        else:
            st.error("Please Input a valid search keyword")        
    except:
        st.error("Please Input a valid search keyword")

