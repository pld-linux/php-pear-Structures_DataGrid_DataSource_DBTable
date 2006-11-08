%include	/usr/lib/rpm/macros.php
%define		_class		Structures
%define		_subclass	DataGrid_DataSource_DBTable
%define		_status		beta
%define		_pearname	Structures_DataGrid_DataSource_DBTable
Summary:	%{_pearname} - DataSource driver using PEAR::DB_Table
Summary(pl):	%{_pearname} - Sterownik DataSource do PEAR::DB_Table
Name:		php-pear-%{_pearname}
Version:	0.1.4
Release:	1
License:	PHP License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	2328071eaef93b9f83a3f8bee88aa598
URL:		http://pear.php.net/package/Structures_DataGrid_DataSource_DBTable/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-pear-DB_Table >= 1.1.0
Requires:	php-pear-PEAR-core >= 1:1.4.9
Requires:	php-pear-Structures_DataGrid >= 0.7.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a DataSource driver for Structures_DataGrid using
PEAR::DB_Table.

In PEAR status of this package is: %{_status}.

%description -l pl
Ten pakiet dostarcza sterownik do PEAR::DB_Table dla
Structures_DataGrid.

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
%{php_pear_dir}/Structures/DataGrid/DataSource/DBTable.php
