# Power Automate expressions

The field names below assume Dataverse dynamic values have been stored in variables with matching names.

## Priority score

```text
min(
  100,
  max(
    0,
    add(
      10,
      mul(
        20,
        add(
          add(
            add(mul(variables('BusinessImpact'),0.20),mul(variables('HoursSavedPotential'),0.15)),
            add(mul(variables('ClientValue'),0.15),mul(variables('StrategicAlignment'),0.15))
          ),
          add(
            add(mul(variables('Feasibility'),0.15),mul(variables('AdoptionReadiness'),0.10)),
            add(mul(variables('Effort'),-0.05),mul(variables('Risk'),-0.05))
          )
        )
      )
    )
  )
)
```

## Expected annual hours saved

```text
div(
  mul(
    mul(
      mul(variables('MonthlyVolume'),12),
      variables('MinutesPerTransaction')
    ),
    variables('AutomationRate')
  ),
  60
)
```

## Human-review condition

```text
or(
  less(variables('MinimumConfidence'),float(parameters('DefaultConfidenceThreshold'))),
  greater(length(variables('HighRiskIndicators')),0)
)
```

## Safe filename check

Use a Switch action on the lower-case extension and allow only the formats approved by firm policy. Terminate the flow for every other extension. File extension checks alone are not malware scanning.

