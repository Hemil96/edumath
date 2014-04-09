edumath
=======
edumath is a python module. You can do calculations of advance topics of mathematics of high school. In intial release v 1.0 it contains 28 functions for performing calculations.

What are the fuctions included?
================================
For matrix operations
----------------------
- det_2c2()
- det_3c3()
- trans_2c2()
- trans_3c3()
- adj_2c2()
- adj_3c3()
- inv_2c2()
- inv_3c3()
- add_2c2()
- add_3c3()
- sub_2c2()
- sub_3c3() 

For progression operations
---------------------------
- ap_term()
- gp_term()
- hp_term()
- ap_sum()
- gp_sum()

For vector operations
----------------------
- mag()
- dot()
- cross()
- box()
- triple()
- angle()
- angx()
- angy()
- angz()
- coplan()
- ortho()

Installation
============
Command line installation on Windows
-------------------------------------
- Keep setup.py and edumath.py in same directory.
- open command prompt and write following
- <code>setup.py install</code>

Command line installation on Linux
-------------------------------------
- Keep setup.py and edumath.py in same directory.
- open command prompt and write following
- <code>python setup.py install</code>

Direct install on 32 bit Windows
---------------------------------
If you wnt to install direct from an installer without using command line then just go to https://sourceforge.net/projects/edumath/ , read README.txt file and download edumath-1.0.win32.exe

Usage
=====

---------------------------------------- Matrix Functions ----------------------------------------

1. edumath.det_2c2(a,b,c,d)
   - This fuction will calculate determinant of two cross two matrix.
   - 'a' and 'b' are elements of first row and 'c' and 'd' are of second row.

2. edumath.det_3c3(a,b,c,d,e,f,g,h,i)
   - This fuction will calculate determinant of three cross three matrix.
   - 'a', 'b', 'c' are of first row, 'd', 'e', 'f' are of second row and 'g', 'h', 'i' are of third row elements.

3. edumath.trans_2c2(a,b,c,d)
   - This function will calculate transpose of two cross two matrix.
   - 'a' and 'b' are elements of first row and 'c' and 'd' are of second row.

4. edumath.trans_3c3(a,b,c,d,e,f,g,h,i)
   - This function will calculate transpose of three cross three matrix.
   - 'a', 'b', 'c' are of first row, 'd', 'e', 'f' are of second row and 'g', 'h', 'i' are of third row elements.

5. edumath.adj_2c2(a,b,c,d)
   - This function will calculate adjoint of two cross two matrix.
   - 'a' and 'b' are elements of first row and 'c' and 'd' are of second row.

6. edumath.adj_3c3(a,b,c,d,e,f,g,h,i)
   - This function will calculate adjoint of three cross three matrix.
   - 'a', 'b', 'c' are of first row, 'd', 'e', 'f' are of second row and 'g', 'h', 'i' are of third row elements.

7. edumath.inv_2c2(a,b,c,d)
   - This function will calculate inverse of two cross two matrix.
   - 'a' and 'b' are elements of first row and 'c' and 'd' are of second row.

8. edumath.inv_3c3(a,b,c,d,e,f,g,h,i)
   - This function will calculate inverse of three cross three matrix.
   - 'a', 'b', 'c' are of first row, 'd', 'e', 'f' are of second row and 'g', 'h', 'i' are of third row elements.

9. edumath.add_2c2(a,b,c,d,aa,bb,cc,dd)
   - This function will calculate addition of two, two cross two matrices.
   - 'a' and 'b' are elements of first row of first matrix and 'c' and 'd' are of second row of first matrix.
   - 'aa' and 'bb' are elements of first row of second matrix and 'cc' and 'dd' are of second row of second matrix.

10. edumath.add_3c3(a,b,c,d,e,f,g,h,i,aa,bb,cc,dd,ee,ff,gg,hh,ii)
   - This function will calculate addition of two, three cross three matrices.
   - 'a', 'b', 'c' are of first row of first matrix, 'd', 'e', 'f' are of second row of first matrix and 'g', 'h', 'i' are of third row of first matrix.
   - 'aa', 'bb', 'cc' are of first row of second matrix, 'dd', 'ee', 'ff' are of second row of second matrix and 'gg', 'hh', 'ii' are of third row of second matrix.

11. edumath.sub_2c2(a,b,c,d,aa,bb,cc,dd)
   - This function will calculate subtraction of two, two cross two matrices.
   - 'a' and 'b' are elements of first row of first matrix and 'c' and 'd' are of second row of first matrix.
   - 'aa' and 'bb' are elements of first row of second matrix and 'cc' and 'dd' are of second row of second matrix.

12. edumath.sub_3c3(a,b,c,d,e,f,g,h,i,aa,bb,cc,dd,ee,ff,gg,hh,ii)
   - This function will calculate subtraction of two, three cross three matrices.
   - 'a', 'b', 'c' are of first row of first matrix, 'd', 'e', 'f' are of second row of first matrix and 'g', 'h', 'i' are of third row of first matrix.
   - 'aa', 'bb', 'cc' are of first row of second matrix, 'dd', 'ee', 'ff' are of second row of second matrix and 'gg', 'hh', 'ii' are of third row of second matrix.

---------------------------------------- Progression Functions ----------------------------------------

13. edumath.ap_term(a,b,c,d)
   - This function will find nth term of an arithmetic progression.
   - 'a', 'b' and 'c' are first, second and third termm of an ap respectively.
   - 'd' is the nth term which you want to find out.

14. edumath.gp_term(a,b,c,d)
   - This function will find nth term of an geometric progression.
   - 'a', 'b' and 'c' are first, second and third termm of an gp respectively.
   - 'd' is the nth term which you want to find out.

15. edumath.hp_term(a,b,c,d)
   - This function will find nth term of an harmonic progression.
   - 'a', 'b' and 'c' are first, second and third termm of an hp respectively.
   - 'd' is the nth term which you want to find out.

16. edumath.ap_sum(a,b,c,d)
   - This function will find fum of first n terms of an arithmetic progression.
   - 'a', 'b' and 'c' are first, second and third termm of an ap respectively.
   - 'd' is the first number of n terms of which you want to calculate sum.

17. edumath.gp_sum(a,b,c,d)
   - This function will find fum of first n terms of an geometric progression.
   - 'a', 'b' and 'c' are first, second and third termm of an gp respectively.
   - 'd' is the first number of n terms of which you want to calculate sum.

---------------------------------------- Vector Functions ----------------------------------------

18. edumath.mag(a,b,c)
   - This function will calculate magnitude of a vector.
   - 'a', 'b' and 'c' are x, y and z components of a vector respectively.

19. edumath.dot(a,b,c,d,e,f)
   - This fuction will calculate dot produst of two vectors.
   - 'a', 'b' and 'c' are x, y and z components of first vector respectively.
   - 'd', 'e' and 'f' are x, y and z components of second vector respectively.

20. edumath.cross(a,b,c,d,e,f)
   - This fuction will calculate cross produst of two vectors.
   - 'a', 'b' and 'c' are x, y and z components of first vector respectively.
   - 'd', 'e' and 'f' are x, y and z components of second vector respectively.

21. edumath.box(a,b,c,d,e,f,g,h,i)
   - This fuction will calculate box produst of three vectors.
   - 'a', 'b' and 'c' are x, y and z components of first vector respectively.
   - 'd', 'e' and 'f' are x, y and z components of second vector respectively.
   - 'g', 'h' and 'i' are x, y and z components of second vector respectively.

22. edumath.triple(a,b,c,d,e,f,g,h,i)
   - This fuction will calculate triple produst of three vectors.
   - 'a', 'b' and 'c' are x, y and z components of first vector respectively.
   - 'd', 'e' and 'f' are x, y and z components of second vector respectively.
   - 'g', 'h' and 'i' are x, y and z components of second vector respectively.

23. edumath.angle(a,b,c,d,e,f)
   - This function will calculate angle between two vectors. (in radian)
   - 'a', 'b' and 'c' are x, y and z components of first vector respectively.
   - 'd', 'e' and 'f' are x, y and z components of second vector respectively.

24. edumath.angx(a,b,c)
   - This function will calculate angle between vector and x-axis.
   - 'a', 'b' and 'c' are x, y and z components of vector respectively.

25. edumath.angy(a,b,c)
   - This function will calculate angle between vector and y-axis.
   - 'a', 'b' and 'c' are x, y and z components of vector respectively.

26. edumath.angz(a,b,c)
   - This function will calculate angle between vector and z-axis.
   - 'a', 'b' and 'c' are x, y and z components of vector respectively.

27. edumath.coplan(a,b,c,d,e,f,g,h,i)
   - This function will return TRUE if three vectors are complannar and if they are no coplannar it returns FALSE.
   - 'a', 'b' and 'c' are x, y and z components of first vector respectively.
   - 'd', 'e' and 'f' are x, y and z components of second vector respectively.
   - 'g', 'h' and 'i' are x, y and z components of second vector respectively.

28. edumath.ORTHO(a,b,c,d,e,f)
   - This function will return TRUE if two vectors are orthogonal and if they are no orthogonal it returns FALSE.
   - 'a', 'b' and 'c' are x, y and z components of first vector respectively.
   - 'd', 'e' and 'f' are x, y and z components of second vector respectively.

Contribution
=============
I started writing this module from 05-04-2014. I covered three topics of high school - Matrices, Progression and Vector Algebra. I am constanly working on edumath. If you find this module helpful and wnt to contribute, then you are allow to contribute on github. (http://www.guthub.com/daxeel/edumath)
I request that insert your code in respective section of mathematics topics. So, in future it can be very easy to maintain edumath project.
In next version release i will give credits to all the contributors.

Bug Fixing
===========
If you found any bug in this module then you can edit it by commiting on github. (http://www.guthub.com/daxeel/edumath)
