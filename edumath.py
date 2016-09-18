#----------------------------------------------------------------------
# Name:        edumath
#
#           1) edumath.py module includes various functions for 
#              calculation of determinant, transpose, adjoint, inverse,
#              addition and subtraction of 2 cross 2 and 3 cross 3
#              matrix/matrices.
#           2) Calculation of nth term of AP-GP-HP and sum of first n 
#              terms of AP and GP.
#           3) Calculation of magnitude, dot-cross-box-triple product,
#              angle between two vectors, angle between vector and  
#              positive X-Axis, Y-Axis, Z-Axis. This module can check
#              whether the vectors are colannar/orthogonal or not.             
#
# Author:      Daxeel Soni
#
# Created:     03-April-2014
#----------------------------------------------------------------------
# edumath 1.0.0 python module for calculations of mathematics topics
# of high school.
#
# Copyright (C) 2014 Daxeel Soni
#
# This software is provided 'as-is', without any express or implied
# warranty.  In no event will the authors be held liable for any damages
# arising from the use of this software.
#
# Permission is granted to anyone to use this software for any purpose,
# including commercial applications, and to alter it and redistribute it
# freely, subject to the following restrictions:
#
# 1. The origin of this software must not be misrepresented; you must not
#    claim that you wrote the original software. If you use this software
#    in a product, an acknowledgment in the product documentation would be
#    appreciated but is not required.
# 2. Altered source versions must be plainly marked as such, and must not be
#    misrepresented as being the original software.
# 3. This notice may not be removed or altered from any source distribution.
#----------------------------------------------------------------------

# ---------------------------- Determinant ----------------------------

def det_2c2(a,b,c,d):
    x = (d * a) - (b * c)
    return(x)
def det_3c3(a,b,c,d,e,f,g,h,i):
    x = (a*((e*i)-(h*f)))-(b*((d*i)-(g*f)))+(c*((d*h)-(e*g)))
    return(x)

# ---------------------------- Transpose ------------------------------

def trans_2c2(a,b,c,d):
    trans_2c2 = [(a,'   ',c),(b,'   ',d)]
    return trans_2c2
def trans_3c3(a,b,c,d,e,f,g,h,i):
    trans_3c3 = [(a,'   ',d,'   ',g),(b,'   ',e,'   ',h),(c,'   ',f,'   ',i)]
    return trans_3c3

# ---------------------------- Adjoint --------------------------------

def adj_2c2(a,b,c,d):
    bb = -1 * b
    cc = -1 * c
    adj_2c2 = [(d,'   ',bb),(cc,'   ',a)]
    return adj_2c2
   
def adj_3c3(a,b,c,d,e,f,g,h,i):
    aa = (e*i)-(h*f)
    bb = (g*f)-(d*i)
    cc = (d*h)-(e*g)
    dd = (c*h)-(b*i)
    ee = (a*i)-(c*g)
    ff = (b*g)-(a*h)
    gg = (f*b)-(e*c)
    hh = (c*d)-(a*f)
    ii = (a*e)-(b*d)
    adj_3c3 = [(aa,'   ',dd,'   ',gg),(bb,'   ',ee,'   ',hh),(cc,'   ',ff,'   ',ii)]
    return adj_3c3
# ---------------------------- Inverse --------------------------------

def inv_2c2(a,b,c,d):
    bb = -1 * b
    cc = -1 * c
    det=(d*a)-(c*b)
    inv_2c2 = [(format(d/det, '.2f'),'     ',format(bb/det, '.2f')),(format(d/det, '.2f'),'     ',format(bb/det, '.2f'))]
    return inv_2c2
def inv_3c3(a,b,c,d,e,f,g,h,i):
    det=(a*((e*i)-(h*f)))-(b*((d*i)-(g*f)))+(c*((d*h)-(e*g)))
    aa = (e*i)-(h*f)
    bb = (g*f)-(d*i)
    cc = (d*h)-(e*g)
    dd = (c*h)-(b*i)
    ee = (a*i)-(c*g)
    ff = (b*g)-(a*h)
    gg = (f*b)-(e*c)
    hh = (c*d)-(a*f)
    ii = (a*e)-(b*d)
    inv_3c3 = [(format(aa/det, '.2f'),'   ',format(dd/det, '.2f'),'   ',format(gg/det, '.2f')),(format(bb/det, '.2f'),'   ',format(ee/det, '.2f'),'   ',format(hh/det, '.2f')),(format(cc/det, '.2f'),'   ',format(ff/det, '.2f'),'   ',format(ii/det, '.2f'))]
    return inv_3c3

# ---------------------------- Addition -------------------------------

def add_2c2(a,b,c,d,aa,bb,cc,dd):
    w = a + aa
    x = b + bb
    y = c + cc
    z = d + dd
    add_2c2 = [(w,'   ',x),(y,'   ',z)]
    return add_2c2
 
def add_3c3(a,b,c,d,e,f,g,h,i,aa,bb,cc,dd,ee,ff,gg,hh,ii):
    r = a + aa
    s = b + bb
    t = c + cc
    u = d + dd
    v = e + ee
    w = f + ff
    x = g + gg
    y = h + hh
    z = i + ii
    add_3c3 = [(r,'   ',s,'   ',t),(u,'   ',v,'   ',w),(x,'   ',y,'   ',z)]
    return adj_3c3
   

# ---------------------------- Subtraction -----------------------------

def sub_2c2(a,b,c,d,aa,bb,cc,dd):
    w = a - aa
    x = b - bb
    y = c - cc
    z = d - dd
    sub_2c2 = [(w,'   ',x),(y,'   ',z)]
    return sub_2c2
   
def sub_3c3(a,b,c,d,e,f,g,h,i,aa,bb,cc,dd,ee,ff,gg,hh,ii):
    r = a - aa
    s = b - bb
    t = c - cc
    u = d - dd
    v = e - ee
    w = f - ff
    x = g - gg
    y = h - hh
    z = i - ii
    sub_3c3 = [(r,'   ',s,'   ',t),(u,'   ',v,'   ',w),(x,'   ',y,'   ',z)]
    return sub_3c3
   
# ---------------------------- AP nth term ------------------------------------

def ap_term(a,b,c,d):
    if (2 * b) == (a + c):
        x = a + ((d - 1) * (b - a))
        return(x)
    else:
        return('Error : ',a,',',b,',',c,' are not in arithmetic progression')

# ---------------------------- GP nth term ------------------------------------

def gp_term(a,b,c,d):
    if (b * b) == (a * c):
        x = a * ((b / a) ** (d - 1))
        return(x)
    else:
        return('Error : ',a,',',b,',',c,' are not in geometric progression')

# ---------------------------- HP nth term ------------------------------------

def hp_term(a,b,c,d):
    if ((1 / b) - (1 / a)) == ((1 / c) - (1 / b)):
        x = 1 / (a + ((d - 1) * (b - a)))
        return(x)
    else:
        return('Error : ',a,',',b,',',c,' are not in harmonic progression')

# ---------------------------- Sum of first n terms of AP ---------------------

def ap_sum(a,b,c,d):
    if (2 * b) == (a + c):
        x = (d / 2) * ((2 * a) + ((d - 1) * (b - a)))
        return(x)
    else:
        return('Error : ',a,',',b,',',c,' are not in arithmetic progression')

# ---------------------------- Sum of first n terms of GP ---------------------

def gp_sum(a,b,c,d):
    if (b * b) == (a * c):
        if (b / a) > 1:
            x = a * ((((b / a) ** d) - 1) / ((b / a) - 1))
            return(x)
        elif (b / a) < 1:
            x = a * ((1 - ((b / a) ** d)) / (1 - (b / a)))
            return(x)
    else:
        return('Error : ',a,',',b,',',c,' are not in geometric progression')

import math

# ---------------------------- Vector Magnitude -----------------------

def mag(a,b,c):
    x = math.sqrt((a * a) + (b * b) + (c * c))
    return(x)
    
# ---------------------------- Vector Products ------------------------

def dot(a,b,c,aa,bb,cc):
    x = (a * aa) + (b * bb) + (c * cc)
    return(x)
def cross(a,b,c,d,e,f):
    x = (b * f) - (e * c)
    y = (c * d) - (a * f)
    z = (a * e) - (b * d)
    return(x,'  ',y,'  ',z)
def box(a,b,c,d,e,f,g,h,i):
    x = (a*((e*i)-(h*f)))-(b*((d*i)-(g*f)))+(c*((d*h)-(e*g)))
    return(x)
def triple(a,b,c,d,e,f,g,h,i):
    x = (a * g) + (b * h) + (c * i)
    y = (a * d) + (b * e) + (c * f)
    xc = (x * d) - (y * g)
    yc = (x * e) - (y * h)
    zc = (x * f) - (y * i)
    return(xc,'',yc,'',zc)

# ------------- Angle between two vectors (in radian) -----------------

def angle(a,b,c,d,e,f):
    xy = (a * d) + (b * e) + (c * f)
    xm = math.sqrt((a * a) + (b * b) + (c * c))
    ym = math.sqrt((d * d) + (e * e) + (f * f))
    xym = xm * ym
    final = xy / xym
    ans = math.acos(final)
    return(ans)

# ------- Angle between vector and positive X-Axis (in radian) ---------

def angx(a,b,c):
    mod = math.sqrt((a * a) + (b * b) + (c * c))
    final = a / mod
    ans = math.acos(final)
    return(ans)

# ------- Angle between vector and positive Y-Axis (in radian) ---------

def angy(a,b,c):
    mod = math.sqrt((a * a) + (b * b) + (c * c))
    final = b / mod
    ans = math.acos(final)
    return(ans)

# ------- Angle between vector and positive Z-Axis (in radian) ---------

def angz(a,b,c):
    mod = math.sqrt((a * a) + (b * b) + (c * c))
    final = c / mod
    ans = math.acos(final)
    return(ans)

# ---------------------- Coplannar Vectors -----------------------------

def coplan(a,b,c,d,e,f,g,h,i):
    x = (a*((e*i)-(h*f)))-(b*((d*i)-(g*f)))+(c*((d*h)-(e*g)))
    if x == 0:
        return('True')
    else:
        return('False')

# ---------------------- Orthogonal Vectors -----------------------------

def ortho(a,b,c,d,e,f):
    x = (a * d) + (b * e) + (c * f)
    if x == 0:
        return('True')
    else:
        return('False')

# ---------------------------- End ------------------------------------

if __name__ == "__main__":
    import doctest
    doctest.testmod()


