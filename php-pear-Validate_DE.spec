%define		_status		alpha
%define		_pearname	Validate_DE
%include	/usr/lib/rpm/macros.php
Summary:	%{_pearname} - Validation class for DE
Summary(pl.UTF-8):	%{_pearname} - Klasa sprawdzająca poprawność dla Niemiec
Name:		php-pear-%{_pearname}
Version:	0.5.2
Release:	3
Epoch:		0
License:	New BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	9b8c94769ad2456f2ab8650863025a11
URL:		http://pear.php.net/package/Validate_DE/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(core) >= 4.1.0
Requires:	php-pear
Obsoletes:	php-pear-Validate_DE-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Package containes locale validation for DE such as:
- Postal Code
- Bank Code

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Pakiet do sprawdzania poprawności dla Niemiec danych takich jak:
- kod pocztowy
- kod banku

Ta klasa ma w PEAR status: %{_status}.

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
