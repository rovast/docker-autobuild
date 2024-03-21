# Text Extraction API

提供 API，分析文本中的实体信息并返回。目前支持的信息如下：

- PERSON: 人名
- NORP: 国籍、宗教或政治团体
- FAC: 建筑、机场、高速公路、桥梁等设施
- ORG: 组织名，包括公司、机构、政府、非政府组织、体育队、媒体名称等
- GPE: 国家、城市、州
- LOC: 非政治区域，如山脉、水体
- PRODUCT: 物品名称，通常不包括食物和饮料
- EVENT: 具体事件，如战役、体育赛事、自然灾害、战争、革命等
- WORK_OF_ART: 文艺作品，如书籍、歌曲名称、电影标题
- LAW: 法律文件名称
- LANGUAGE: 语言名称
- DATE: 绝对或相对日期，或日期范围
- TIME: 时间描述，不包含日期，如“午夜”、“一年中的最后一刻”
- PERCENT: 百分比描述
- MONEY: 金钱数额
- QUANTITY: 测量数量，如距离、重量等
- ORDINAL: 序数词，如“第一”、“第二”
- CARDINAL: 数字，不属于其他类型

## 安装项目

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

## 运行

```bash
uvicorn app.main:app --reload
```


## 调用

POST `/extract/`:

```json
{
  "text": "Meet me at Times Square at 3pm for a show that costs $29.99."
}
```

返回
```json
[
    {
        "label": "FAC",
        "text": "Times Square"
    },
    {
        "label": "TIME",
        "text": "3pm"
    },
    {
        "label": "MONEY",
        "text": "29.99"
    }
]
```

## Docker

```bash
docker build -t ticktin-ai:latest .

docker-compose up --build
```
