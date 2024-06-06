@echo off 
set list=en zh-cn 
(for %%a in (%list%) do ( 
   sphinx-build -M html %%a %%a/_build
))