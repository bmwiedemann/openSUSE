local k = import 'ksonnet/ksonnet.beta.3/k.libsonnet';
local pvc = k.core.v1.persistentVolumeClaim;

local kp =
  (import 'kube-prometheus/kube-prometheus.libsonnet') +
  (import 'kube-prometheus/kube-prometheus-node-ports.libsonnet') +
  (import 'kube-prometheus/kube-prometheus-kubeadm.libsonnet') +
  (import 'kube-prometheus/kube-prometheus-weave-net.libsonnet') +
  {
    _config+:: {
      namespace: 'monitoring',

      //versions+:: {
      //  alertmanager: "v0.20.0",
      //  nodeExporter: "v0.18.1",
      //  kubeStateMetrics: "v1.5.0",
      //  kubeRbacProxy: "v0.4.1",
      //  prometheusOperator: "v0.36.0",
      //  prometheus: "v2.15.2",
      //},

      imageRepos+:: {
        prometheus: "quay.io/prometheus/prometheus",
        alertmanager: "quay.io/prometheus/alertmanager",
        kubeStateMetrics: "quay.io/coreos/kube-state-metrics",
        kubeRbacProxy: "quay.io/coreos/kube-rbac-proxy",
        nodeExporter: "quay.io/prometheus/node-exporter",
        prometheusOperator: "quay.io/coreos/prometheus-operator",
      },
    },

    prometheusAlerts+:: {
      groups: std.map(
        function(group)
          if group.name == 'weave-net' then
            group {
              rules: std.map(function(rule)
                if rule.alert == "WeaveNetFastDPFlowsLow" then
                  rule {
                    expr: "sum(weave_flows) < 20000"
                  }
                else if rule.alert == "WeaveNetIPAMUnreachable" then
                  rule {
                    expr: "weave_ipam_unreachable_percentage > 25"
                  }
                else
                  rule
                ,
                group.rules
              )
            }
          else
            group,
          super.groups
        ),
    },

    prometheus+:: {
      prometheus+: {
        spec+: {
          retention: '30d',
          storage: {
            volumeClaimTemplate:
              pvc.new() +
                pvc.mixin.spec.withAccessModes('ReadWriteOnce') +
                pvc.mixin.spec.resources.withRequests({ storage: '10Gi' }) +
                pvc.mixin.spec.withStorageClassName('managed-nfs-storage'),
            },
          },
        },
      },

    grafana+:: {
      deployment+: {
        spec+: {
          template+: {
            spec+: {
              volumes:
                std.map(
                        function(v)
                            if v.name == 'grafana-storage' then
                            {'name':'grafana-storage',
                                'persistentVolumeClaim': {
                                    'claimName': 'grafana-storage'}
                            }
                            else
                                v,
                    super.volumes
                    ),
                },
            },
            },
        },
        storage:
            local pvc = k.core.v1.persistentVolumeClaim;
            pvc.new() + pvc.mixin.metadata.withNamespace($._config.namespace) +
                        pvc.mixin.metadata.withName("grafana-storage") +
                        pvc.mixin.spec.withStorageClassName('managed-nfs-storage') +
                        pvc.mixin.spec.withAccessModes('ReadWriteMany') +
                        pvc.mixin.spec.resources.withRequests({ storage: '200Mi' }),
    },

  };

// Uncomment line below to enable vertical auto scaling of kube-state-metrics
//{ ['ksm-autoscaler-' + name]: kp.ksmAutoscaler[name] for name in std.objectFields(kp.ksmAutoscaler) } +
{ ['setup/0namespace-' + name]: kp.kubePrometheus[name] for name in std.objectFields(kp.kubePrometheus) } +
{
  ['setup/prometheus-operator-' + name]: kp.prometheusOperator[name]
  for name in std.filter((function(name) name != 'serviceMonitor'), std.objectFields(kp.prometheusOperator))
} +
// serviceMonitor is separated so that it can be created after the CRDs are ready
{ 'prometheus-operator-serviceMonitor': kp.prometheusOperator.serviceMonitor } +
{ ['node-exporter-' + name]: kp.nodeExporter[name] for name in std.objectFields(kp.nodeExporter) } +
{ ['kube-state-metrics-' + name]: kp.kubeStateMetrics[name] for name in std.objectFields(kp.kubeStateMetrics) } +
{ ['alertmanager-' + name]: kp.alertmanager[name] for name in std.objectFields(kp.alertmanager) } +
{ ['prometheus-' + name]: kp.prometheus[name] for name in std.objectFields(kp.prometheus) } +
{ ['prometheus-adapter-' + name]: kp.prometheusAdapter[name] for name in std.objectFields(kp.prometheusAdapter) } +
{ ['grafana-' + name]: kp.grafana[name] for name in std.objectFields(kp.grafana) }
