Summary:	Python interface to the cephes library 
Name:		python-numpy-cephes
Version:	0.71
Release:	1
Copyright:	Distributable
Group:		Development/Languages/Python
Group(de):	Entwicklung/Sprachen/Python
Group(pl):	Programowanie/Jêzyki/Python
Source0:	cephes-%{version}.tgz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	python >= 1.5, python-numpy >= 1.3

%description 
Special functions for Numerical python.

Cephes is a collection of routines which work on arbitrary multiarrays
defined by Numerical Python. It defines functions such as bessel,
error, and elliptic integrals. It is based on the cephes library
available from netlib.org.

%prep
%setup -q -n cephes

%build
%{__make} OPT="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/NumPy
install *.so $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/NumPy

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/cephes.txt README
%doc docs/included_functions.html
%{_libdir}/python1.5/site-packages/NumPy/cephesmodule.so
