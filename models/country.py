from pydantic import BaseModel, Field
from assets_data.country_data import country_data


class Country(BaseModel):
    capital: str = Field(..., alias="capital")
    country_flag: str = Field(..., alias="country-flag")
    country_flag_svg: str = Field(..., alias="country-flag-svg")
    currency_code: str = Field(..., alias="currency-code")
    currency_name: str = Field(..., alias="currency-name")
    currency_symbol: str = Field(..., alias="currency-symbol")
    iso_a2: str = Field(..., alias="iso-a2")
    iso_a3: str = Field(..., alias="iso-a3")
    iso_num: int = Field(..., alias="iso-num")
    name: str = Field(..., alias="name")
    slug: str = Field(..., alias="slug")
    state_name: str = Field(..., alias="state-name")
    region_2: str = Field(..., alias="region-2")

    class Config:
        populate_by_name = True

    @classmethod
    def set_country_model_data(cls):
        countries = []
        for item in country_data:
            country = cls(**item)
            countries.append(country)
        return countries
