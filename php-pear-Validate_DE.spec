%include	/usr/lib/rpm/macros.php
%define		_class		Validate
%define		_subclass	DE
%define		_status		alpha
%define		_pearname	Validate_DE

Summary:	%{_pearname} - Validation class for DE
Summary(pl):	%{_pearname} - Klasa sprawdzaj�ca poprawno�� dla Niemiec
Name:		php-pear-%{_pearname}
Version:	0.5.1
Release:	1
License:	New BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	6e5f522a8e48a2ef47ac5678b39fd929
URL:		http://pear.php.net/package/Validate_DE/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-common >= 3:4.1.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Package containes locale validation for DE such as:
- Postal Code
- Bank Code

In PEAR status of this package is: %{_status}.

%description -l pl
Pakiet do sprawdzania poprawno�ci dla Niemiec:
- kod pocztowy
- kod banku

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Validate/DE.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/Validate_DE/tests/validate_DE.phpt
