@echo off 
set list=en zh
(for %%a in (%list%) do ( 
   sphinx-build -M html %%a %%a/_build
))