export class Myslak {
  constructor(
    public name: string,
    public description: string,
    public outline_color: string,
    public filling_color: string,
    public background: number,
    public cloth: number,
    public head: number,
    public id?: number,
    public updatedAt?: Date,
    public createdAt?: Date,
    public lastUpdatedBy?: string,
  ) {
  }
}
