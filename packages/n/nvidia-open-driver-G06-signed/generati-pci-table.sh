#!/bin/sh

if [ $# -ne 1 ]; then
    echo "$0 <input_file"
    exit 1
fi

input=$1

cat > nvidia/nv_pci_table_list.h <<EOF
EOF
cat > nvidia/nv_module_pci_table_list.h <<EOF
EOF
for did in $(cat $input | cut -d " " -f1 ); do
    echo $did
    cat >> nvidia/nv_pci_table_list.h <<EOF
    {
        .vendor      = PCI_VENDOR_ID_NVIDIA,
        .device      = $did,
        .subvendor   = PCI_ANY_ID,
        .subdevice   = PCI_ANY_ID,
        .class       = (PCI_CLASS_DISPLAY_VGA << 8),
        .class_mask  = ~0
    },
    {
        .vendor      = PCI_VENDOR_ID_NVIDIA,
        .device      = $did,
        .subvendor   = PCI_ANY_ID,
        .subdevice   = PCI_ANY_ID,
        .class       = (PCI_CLASS_DISPLAY_3D << 8),
        .class_mask  = ~0
    },
EOF

    cat >> nvidia/nv_module_pci_table_list.h <<EOF
    {
        .vendor      = PCI_VENDOR_ID_NVIDIA,
        .device      = $did,
        .subvendor   = PCI_ANY_ID,
        .subdevice   = PCI_ANY_ID,
        .class       = (PCI_CLASS_DISPLAY_VGA << 8),
        .class_mask  = ~0
    },
    {
        .vendor      = PCI_VENDOR_ID_NVIDIA,
        .device      = $did,
        .subvendor   = PCI_ANY_ID,
        .subdevice   = PCI_ANY_ID,
        .class       = (PCI_CLASS_DISPLAY_3D << 8),
        .class_mask  = ~0
    },
    {
        .vendor      = PCI_VENDOR_ID_NVIDIA,
        .device      = $did,
        .subvendor   = PCI_ANY_ID,
        .subdevice   = PCI_ANY_ID,
        .class       = (PCI_CLASS_BRIDGE_OTHER << 8),
        .class_mask  = ~0
    },
EOF
done
cp nvidia/nv_pci_table_list.h nvidia-drm/nv_pci_table_list.h
cp nvidia/nv_module_pci_table_list.h nvidia-drm/nv_module_pci_table_list.h
