from datetime import datetime

import matplotlib as mpl
import palmerpenguins
import seaborn as sns
import streamlit as st

penguins = palmerpenguins.load_penguins()

 # Create a (scatter) plot object.
   # f, ax = mpl.subplots(1,1)
g = sns.relplot(
  data=penguins,
  x='bill_length_mm',
  y='bill_depth_mm',
  hue='species'
)

g.set_axis_labels('Bill length (mm)', 'Bill depth (mm)')
g.set(title='Bill length and depth correlation across species')
   # Add the object to the page.

st.pyplot(g)

