export class Myslak {
  constructor(
    public title: string,
    public description: string,
    public background_url: string,
    public _id?: number,
    public updatedAt?: Date,
    public createdAt?: Date,
    public lastUpdatedBy?: string,
  ) {
  }
}
