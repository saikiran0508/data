Filtered_Count :=
VAR SelectedType = VALUES('Table'[Fraud_Type])
RETURN
CALCULATE(
    COUNTROWS('Table'),
    FILTER(
        'Table',
        'Table'[Fraud_Type] = "New"
        || 'Table'[Fraud_Type] IN SelectedType
    )
)
