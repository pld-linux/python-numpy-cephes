
%define mname cephes

Summary:	Python interface to the cephes library
Summary(pl):	Interfejs Pythona do biblioteki cephes
Name:		python-numpy-cephes
Version:	1.3
Release:	1
License:	distributable
Group:		Development/Languages/Python
Group(de):	Entwicklung/Sprachen/Python
Group(pl):	Programowanie/Jêzyki/Python
Source0:	http://pylab.sourceforge.net/packages/%{mname}-%{version}.tar.gz
URL:		http://pylab.sourceforge.net/
BuildRequires:	python-devel >= 1.5
BuildRequires:	python-numpy-devel >= 1.3
Requires:	python-numpy >= 1.3
%requires_eq	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%include /usr/lib/rpm/macros.python

%description 
Special functions for Numerical python.

Cephes is a collection of routines which work on arbitrary multiarrays
defined by Numerical Python. It defines functions such as bessel,
error, and elliptic integrals. It is based on the cephes library
available from netlib.org.

%description -l pl
Cephes to zestaw funkcji dzia³aj±cych z tablicami zdefiniowanymi w
module Numerical Python. Zawieraj± funkcje takie jak bessel, b³±d,
ca³ki eliptyczne. Bazuje na bibliotece cephes dostêpnej z netlib.org.

%prep
%setup -q -n %{mname}-%{version}

%build
%{__make} OPT="%{rpmcflags}" \
	INCLUDES="-I%{_includedir}/python%{py_ver} -I%{_includedir}/python%{py_ver}/Numeric"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitedir}/NumPy
install *.so $RPM_BUILD_ROOT%{py_sitedir}/NumPy

gzip -9nf docs/included_functions.html docs/cephes.txt README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/included_functions.html* docs/cephes.txt* README*
%{py_sitedir}/NumPy/cephesmodule.so
