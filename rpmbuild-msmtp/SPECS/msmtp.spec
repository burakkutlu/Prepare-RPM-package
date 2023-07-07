Name:           msmtp
Version:        1.8.24
Release:        1%{?dist}
Summary:        Rpm package for msmtp

License:        GPLv3+
URL:            https://marlam.de/msmtp/releases/%{name}-%{version}.tar.xz
Source0:        %{name}-%{version}.tar.xz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gettext
Requires:       bash

%description
The long-tail description for msmtp

%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
./configure
make
make install
mkdir -p %{buildroot}/usr/local/bin
cp -r /usr/local/bin/%{name} %{buildroot}/usr/local/bin


%files
/usr/local/bin/msmtp

%changelog
* Wed Jul  5 2023 root
- 
