from django.db import models
    
CATEGORY = (('言質', '言質'), ('紹介', '紹介'), ('終了', '終了'), ('再度アポ', '再度アポ'))
PROVNAME = {
    '北海道': '北海道', '青森県': '青森', '岩手県': '岩手', '宮城県': '宮城', '秋田県': '秋田', '山形県': '山形', '福島県': '福島', 
    '茨城県': '茨城', '栃木県': '栃木', '群馬県': '群馬', '埼玉県': '埼玉', '千葉県': '千葉', '東京都': '東京', '神奈川県': '神奈川', 
    '新潟県': '新潟', '富山県': '富山', '石川県': '石川', '福井県': '福井', '山梨県': '山梨', '長野県': '長野', 
    '岐阜県': '岐阜', '静岡県': '静岡', '愛知県': '愛知', '三重県': '三重', '滋賀県': '滋賀', 
    '京都府': '京都', '大阪府': '大阪', '兵庫県': '兵庫', '奈良県': '奈良', '和歌山県': '和歌山', 
    '鳥取県': '鳥取', '島根県': '島根', '岡山県': '岡山', '広島県': '広島', '山口県': '山口', 
    '徳島県': '徳島', '香川県': '香川', '愛媛県': '愛媛', '高知県': '高知', 
    '福岡県': '福岡', '佐賀県': '佐賀', '長崎県': '長崎', '熊本県': '熊本', '大分県': '大分', '宮崎県': '宮崎', '鹿児島県': '鹿児島', '沖縄県': '沖縄'
}
WORK = {
    '農業、林業': '農業、林業', '漁業': '漁業', '鉱業、採石業、砂利採取業': '鉱業、採石業、砂利採取業', '建設業': '建設業',
    '製造業': '製造業', '電気・ガス・熱供給・水道業': '電気・ガス・熱供給・水道業', '情報通信業': '情報通信業',
    '運輸業、郵便業': '運輸業、郵便業', '卸売業・小売業': '卸売業・小売業', '金融業・保険業': '金融業・保険業',
    '不動産業、物品賃貸業': '不動産業、物品賃貸業', '学術研究、専門・技術サービス業': '学術研究、専門・技術サービス業',
    '宿泊業、飲食サービス業': '宿泊業、飲食サービス業', '生活関連サービス業、娯楽業': '生活関連サービス業、娯楽業',
    '教育、学習支援業': '教育、学習支援業', '医療、福祉': '医療、福祉', '複合サービス事業': '複合サービス事業',
    'その他':'その他'
}
WANTS = {
    '稼ぎたい': '稼ぎたい', '独立': '独立', '恋愛':'恋愛', 'コミュニティ作り': 'コミュニティ作り', '移動': '引っ越し', '不明': '不明'
}

# class User(models.Model):
#     user_name = models.CharField(max_length=255, primary_key=True)
#     password = models.CharField(max_length=50)

from accounts.models import User

class CustomerInformation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    work = models.CharField(max_length=100,
                            choices= WORK)
    business = models.CharField(max_length=100,
                                null=True, blank=True)
    place = models.CharField(max_length=100,
                             choices= PROVNAME)
    wants = models.CharField(max_length=100,
                             choices=WANTS)
    result = models.CharField(max_length=100,
                              choices = CATEGORY)
    other = models.TextField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)