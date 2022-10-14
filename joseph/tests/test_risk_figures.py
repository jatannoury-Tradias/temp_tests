import config
import joseph.APIs.risk_figures as risk_figures
ENVIRONMENT = 'otcapp-UAT'
from decimal import *
getcontext().prec=1

headers = {
  'Accept': 'application/json',
  'Authorization': f'Bearer {config.UAT_TOKEN3}'
}
wrong_headers = {
  'Accept': 'application/json',
  'Authorization': f'Bearer {config.WRONG_TOKEN}'
}


class TestRiskFigures:

    def test_sanity_checks(self):
        response=risk_figures.getRiskFigures().json()
        assert Decimal(str(response['exposure_in_eur']))/Decimal(str(response['margin_usage']))==Decimal(str(response['maximum_exposure']))
        assert type(response['exposure_in_eur'])==float and type(response['maximum_exposure'])==float and type(response['margin_usage'])==float
        assert response['exposure_in_eur']>0 and response['maximum_exposure']>0 and response['margin_usage']>0 and response['margin_requirement']>0
        if response['margin_usage']>1:
            assert response['exposure_in_eur']>response['maximum_exposure']
        else:
            assert response['exposure_in_eur']<response['maximum_exposure']

    def test_get_risk_figures_with_wrong_headers_fail(self):
        assert risk_figures.getRiskFigures(wrong_header=True).json()=={'error': 'Invalid Authorization Bearer Token'}


