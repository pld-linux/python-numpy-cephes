Summary: Python interface to the cephes library 
Name: python-numpy-cephes
Version: 0.71
Release: 1
Copyright: Distributable
Packager: Travis Oliphant <Oliphant.Travis@mayo.edu>
Group: Development/Languages/Python
Source0: cephes-0.71.tgz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires: python >= 1.5, python-numpy >= 1.3

%description 
Special functions for Numerical python

Cephes is a collection of routines which work on arbitrary 
multiarrays defined by Numerical Python.  It defines functions such
as bessel, error, and elliptic integrals.  It is based on the cephes 
library available from netlib.org

%prep
%setup -n cephes

%build
%{__make} OPT="$RPM_OPT_FLAGS"

%install
install -d $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/NumPy
cp *.so $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/NumPy

%clean
rm -rf $RPM_BUILD_ROOT

%post

%files
%doc docs/cephes.txt README
%doc docs/included_functions.html
%{_libdir}/python1.5/site-packages/NumPy/cephesmodule.so
