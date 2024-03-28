from dataclasses import dataclass
from datetime import datetime
import skinport


@dataclass
class Bargain:
    market_name: str
    name: str
    url: str
    image: str
    rarity_color: int
    wear: float
    exterior: str
    lock: datetime
    price: float
    suggested_price: float
    discount: float
    last_7_days: skinport.LastXDays
    last_30_days: skinport.LastXDays
    last_90_days: skinport.LastXDays

    def get_wear_str(self, minimal: bool = False):
        if minimal:
            return f"{self.wear:.3f}" if self.wear else "N/A"
        return f"{self.wear:.3f} | {self.exterior}" if self.wear else "N/A"

    def get_lock_str(self, minimal: bool = False):
        format = "%d/%m %H:%M" if not minimal else "%d/%m"
        return self.lock.strftime(format) if self.lock else "Tradable"

    def get_7d_str(self):
        return (
            f"{self.last_7_days.min} / {self.last_7_days.avg} / {self.last_7_days.max}"
        )

    def get_30d_str(self):
        return f"{self.last_30_days.min} / {self.last_30_days.avg} / {self.last_30_days.max}"

    def get_90d_str(self):
        return f"{self.last_90_days.min} / {self.last_90_days.avg} / {self.last_90_days.max}"

    def get_color_str(self):
        return f"#{self.rarity_color:x}"
