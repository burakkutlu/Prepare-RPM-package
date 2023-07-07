Name:           netflow2ng
Version:        0.0.4
Release:        1%{?dist}
Summary:        Rpm package for netflow2ng

License:        MIT
URL:            https://github.com/synfinatic/%{name}
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  golang
BuildRequires:  make
BuildRequires:	epel-release
BuildRequires:	zeromq-devel
Requires:       bash      

%description
The long-tail description for netflow2ng

%prep
%setup -q

%global debug_package %{nil}

%build
go mod download github.com/alecthomas/assert/v2
make %{?_smp_mflags}


%install 
mkdir -p %{buildroot}/usr/local/bin
cp dist/netflow2ng-0.0.4 %{buildroot}/usr/local/bin

%files
/usr/local/bin/netflow2ng-0.0.4

%changelog
* Tue Jul  4 2023 root
- 
