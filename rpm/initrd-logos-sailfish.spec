Name:       initrd-logos-sailfish
Summary:    Sailfish logos for init ramdisks
Version:    0.0.1
Release:    1
Group:      System/Boot
License:    GPLv2
Source0:    %{name}-%{version}.tar.gz

Provides:   initrd-logos

%description
%{summary}

%prep
%setup -q -n %{name}-%{version}

%build

%install
mkdir -p %{buildroot}/usr/share/initrd-logos
cp images/*  %{buildroot}/usr/share/initrd-logos/

%files
%defattr(-,root,root,-)
/usr/share/initrd-logos

%doc LICENSE README
