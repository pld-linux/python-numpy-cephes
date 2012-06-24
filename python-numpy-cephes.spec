%include /usr/lib/rpm/macros.python
%define mname cephes

Summary:	Python interface to the cephes library
Summary(pl):	Interfejs Pythona do biblioteki cephes
Name:		python-numpy-cephes
Version:	1.3
Release:	2
License:	distributable
Group:		Development/Languages/Python
Source0:	http://pylab.sourceforge.net/packages/%{mname}-%{version}.tar.gz
# Source0-md5:	55de90ee4f2d48e8da6054d0a5f4dd74
URL:		http://pylab.sourceforge.net/
BuildRequires:	python-devel >= 1.5
BuildRequires:	python-numpy-devel >= 1.3
BuildRequires:	rpm-pythonprov
Requires:	python-numpy >= 1.3
%pyrequires_eq	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Special functions for Numerical python.

Cephes is a collection of routines which work on arbitrary multiarrays
defined by Numerical Python. It defines functions such as bessel,
error, and elliptic integrals. It is based on the cephes library
available from netlib.org.

%description -l pl
Cephes to zestaw funkcji operuj�cych na tablicach zdefiniowanych w
module Numerical Python. Zawieraj� funkcje takie jak bessel, b��d,
ca�ki eliptyczne. Bazuje na bibliotece cephes dost�pnej z netlib.org.

%prep
%setup -q -n %{mname}-%{version}

%build
%{__make} OPT="%{rpmcflags}" \
	INCLUDES="-I%{py_incdir} -I%{py_incdir}/Numeric"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitedir}/NumPy
install *.so $RPM_BUILD_ROOT%{py_sitedir}/NumPy

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/included_functions.html docs/cephes.txt README
%{py_sitedir}/NumPy/cephesmodule.so
